import json
import os
import random

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset

from backend.evaluation.tokenizer import InterviewTokenizer
from backend.evaluation.transformer_model import InterviewTransformer


DATA_PATH = "data/interview_answers.json"
MODEL_PATH = "models/interview_evaluator.pt"


SEED = 42

random.seed(SEED)
torch.manual_seed(SEED)


# --------------------------------------------------
# Configuration
# --------------------------------------------------

BATCH_SIZE = 32
EPOCHS = 40

LEARNING_RATE = 0.0002

MAX_LENGTH = 128

D_MODEL = 160
NUM_HEADS = 4
FEED_FORWARD_DIMENSION = 512
NUM_LAYERS = 3
DROPOUT = 0.2

NUM_CLASSES = 5


# --------------------------------------------------
# Dataset
# --------------------------------------------------

class InterviewDataset(Dataset):

    def __init__(
        self,
        data,
        tokenizer
    ):
        self.data = data
        self.tokenizer = tokenizer

    def __len__(self):

        return len(self.data)

    def __getitem__(self, index):

        item = self.data[index]

        # Encode:
        #
        # question <sep> answer
        #
        token_ids = self.tokenizer.encode_pair(
            item["question"],
            item["answer"],
            max_length=MAX_LENGTH
        )

        input_ids = torch.tensor(
            token_ids,
            dtype=torch.long
        )

        label = torch.tensor(
            item["label"],
            dtype=torch.long
        )

        return input_ids, label


# --------------------------------------------------
# Load dataset
# --------------------------------------------------

def load_data():

    with open(
        DATA_PATH,
        "r"
    ) as file:

        data = json.load(file)

    # --------------------------------------------------
    # IMPORTANT:
    # Split using unique questions.
    #
    # This prevents answers belonging to the same
    # question from appearing in both train and test.
    # --------------------------------------------------

    questions = list(
        dict.fromkeys(
            item["question"]
            for item in data
        )
    )

    random.shuffle(questions)

    total_questions = len(questions)

    train_end = int(
        total_questions * 0.70
    )

    validation_end = int(
        total_questions * 0.85
    )

    train_questions = set(
        questions[:train_end]
    )

    validation_questions = set(
        questions[
            train_end:validation_end
        ]
    )

    test_questions = set(
        questions[
            validation_end:
        ]
    )

    train_data = [
        item
        for item in data
        if item["question"] in train_questions
    ]

    validation_data = [
        item
        for item in data
        if item["question"] in validation_questions
    ]

    test_data = [
        item
        for item in data
        if item["question"] in test_questions
    ]

    return (
        train_data,
        validation_data,
        test_data
    )


# --------------------------------------------------
# Build tokenizer
# --------------------------------------------------

def build_tokenizer(train_data):

    tokenizer = InterviewTokenizer()

    # Build vocabulary ONLY from training data.
    #
    # This prevents validation/test information
    # from leaking into the vocabulary.

    tokenizer.build_vocab_from_dataset(
        train_data
    )

    return tokenizer


# --------------------------------------------------
# Device
# --------------------------------------------------

def get_device():

    if torch.backends.mps.is_available():

        return torch.device("mps")

    return torch.device("cpu")


# --------------------------------------------------
# Evaluation
# --------------------------------------------------

def evaluate(
    model,
    loader,
    device,
    loss_function
):

    model.eval()

    total_loss = 0.0
    correct = 0
    total = 0

    all_predictions = []
    all_labels = []

    with torch.no_grad():

        for input_ids, labels in loader:

            input_ids = input_ids.to(
                device
            )

            labels = labels.to(
                device
            )

            logits = model(
                input_ids
            )

            loss = loss_function(
                logits,
                labels
            )

            total_loss += (
                loss.item()
                * labels.size(0)
            )

            predictions = torch.argmax(
                logits,
                dim=1
            )

            correct += (
                predictions == labels
            ).sum().item()

            total += labels.size(0)

            all_predictions.extend(
                predictions.cpu().tolist()
            )

            all_labels.extend(
                labels.cpu().tolist()
            )

    average_loss = (
        total_loss / total
    )

    accuracy = (
        correct / total
    ) * 100

    return (
        average_loss,
        accuracy,
        all_labels,
        all_predictions
    )


# --------------------------------------------------
# Classification metrics
# --------------------------------------------------

def calculate_metrics(
    labels,
    predictions,
    num_classes=NUM_CLASSES
):

    confusion_matrix = [
        [0 for _ in range(num_classes)]
        for _ in range(num_classes)
    ]

    for actual, predicted in zip(
        labels,
        predictions
    ):

        confusion_matrix[actual][predicted] += 1

    precisions = []
    recalls = []
    f1_scores = []

    for class_index in range(
        num_classes
    ):

        true_positive = (
            confusion_matrix[class_index][class_index]
        )

        false_positive = sum(
            confusion_matrix[row][class_index]
            for row in range(num_classes)
            if row != class_index
        )

        false_negative = sum(
            confusion_matrix[class_index][column]
            for column in range(num_classes)
            if column != class_index
        )

        if (
            true_positive + false_positive
            > 0
        ):

            precision = (
                true_positive
                / (
                    true_positive
                    + false_positive
                )
            )

        else:

            precision = 0.0

        if (
            true_positive + false_negative
            > 0
        ):

            recall = (
                true_positive
                / (
                    true_positive
                    + false_negative
                )
            )

        else:

            recall = 0.0

        if (
            precision + recall
            > 0
        ):

            f1 = (
                2
                * precision
                * recall
                / (precision + recall)
            )

        else:

            f1 = 0.0

        precisions.append(precision)
        recalls.append(recall)
        f1_scores.append(f1)

    macro_precision = (
        sum(precisions)
        / num_classes
    )

    macro_recall = (
        sum(recalls)
        / num_classes
    )

    macro_f1 = (
        sum(f1_scores)
        / num_classes
    )

    return (
        macro_precision,
        macro_recall,
        macro_f1,
        confusion_matrix
    )


# --------------------------------------------------
# Print confusion matrix
# --------------------------------------------------

def print_confusion_matrix(
    confusion_matrix
):

    print("\nConfusion Matrix:")
    print()

    print(
        "Actual \\ Predicted | "
        "0     1     2     3     4"
    )

    print(
        "-" * 38
    )

    for index, row in enumerate(
        confusion_matrix
    ):

        values = " ".join(
            f"{value:5d}"
            for value in row
        )

        print(
            f"{index:^17} | {values}"
        )


# --------------------------------------------------
# Main training
# --------------------------------------------------

def main():

    print("=" * 60)
    print("CUSTOM TRANSFORMER TRAINING")
    print("=" * 60)

    # --------------------------------------------------
    # Load data
    # --------------------------------------------------

    (
        train_data,
        validation_data,
        test_data
    ) = load_data()

    print(
        "\nTraining examples:",
        len(train_data)
    )

    print(
        "Validation examples:",
        len(validation_data)
    )

    print(
        "Test examples:",
        len(test_data)
    )

    # Count unique questions
    train_questions = len(
        set(
            item["question"]
            for item in train_data
        )
    )

    validation_questions = len(
        set(
            item["question"]
            for item in validation_data
        )
    )

    test_questions = len(
        set(
            item["question"]
            for item in test_data
        )
    )

    print(
        "\nUnique training questions:",
        train_questions
    )

    print(
        "Unique validation questions:",
        validation_questions
    )

    print(
        "Unique test questions:",
        test_questions
    )

    # --------------------------------------------------
    # Tokenizer
    # --------------------------------------------------

    tokenizer = build_tokenizer(
        train_data
    )

    print(
        "\nVocabulary size:",
        len(tokenizer.vocab)
    )

    print(
        "PAD token:",
        tokenizer.vocab["<pad>"]
    )

    print(
        "UNK token:",
        tokenizer.vocab["<unk>"]
    )

    print(
        "SEP token:",
        tokenizer.vocab["<sep>"]
    )

    # --------------------------------------------------
    # Datasets
    # --------------------------------------------------

    train_dataset = InterviewDataset(
        train_data,
        tokenizer
    )

    validation_dataset = InterviewDataset(
        validation_data,
        tokenizer
    )

    test_dataset = InterviewDataset(
        test_data,
        tokenizer
    )

    # --------------------------------------------------
    # DataLoaders
    # --------------------------------------------------

    train_loader = DataLoader(
        train_dataset,
        batch_size=BATCH_SIZE,
        shuffle=True
    )

    validation_loader = DataLoader(
        validation_dataset,
        batch_size=BATCH_SIZE,
        shuffle=False
    )

    test_loader = DataLoader(
        test_dataset,
        batch_size=BATCH_SIZE,
        shuffle=False
    )

    # --------------------------------------------------
    # Device
    # --------------------------------------------------

    device = get_device()

    print(
        "\nTraining device:",
        device
    )

    # --------------------------------------------------
    # Model
    # --------------------------------------------------

    model = InterviewTransformer(
        vocab_size=len(
            tokenizer.vocab
        ),
        num_classes=NUM_CLASSES,
        max_length=MAX_LENGTH,
        d_model=D_MODEL,
        num_heads=NUM_HEADS,
        feed_forward_dimension=(
            FEED_FORWARD_DIMENSION
        ),
        num_layers=NUM_LAYERS,
        dropout=DROPOUT
    )

    model = model.to(
        device
    )

    # --------------------------------------------------
    # Loss
    # --------------------------------------------------

    loss_function = nn.CrossEntropyLoss(label_smoothing=0.05)
    # --------------------------------------------------
    # Optimizer
    # --------------------------------------------------

    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=LEARNING_RATE,
        weight_decay=0.01
    )

    # --------------------------------------------------
    # Learning-rate scheduler
    # --------------------------------------------------

    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optimizer,
        mode="min",
        factor=0.5,
        patience=3
    )

    # --------------------------------------------------
    # Best validation loss
    # --------------------------------------------------

    best_validation_loss = float(
        "inf"
    )

    patience = 7
    epochs_without_improvement = 0

    os.makedirs(
        "models",
        exist_ok=True
    )

    # --------------------------------------------------
    # Training loop
    # --------------------------------------------------

    for epoch in range(
        EPOCHS
    ):

        model.train()

        total_training_loss = 0.0
        total_training_examples = 0

        for input_ids, labels in train_loader:

            input_ids = input_ids.to(
                device
            )

            labels = labels.to(
                device
            )

            optimizer.zero_grad()

            logits = model(
                input_ids
            )

            loss = loss_function(
                logits,
                labels
            )

            loss.backward()

            torch.nn.utils.clip_grad_norm_(
                model.parameters(),
                max_norm=1.0
            )

            optimizer.step()

            total_training_loss += (
                loss.item()
                * labels.size(0)
            )

            total_training_examples += (
                labels.size(0)
            )

        training_loss = (
            total_training_loss
            / total_training_examples
        )

        (
            validation_loss,
            validation_accuracy,
            _,
            _
        ) = evaluate(
            model,
            validation_loader,
            device,
            loss_function
        )

        scheduler.step(
            validation_loss
        )

        current_lr = optimizer.param_groups[0]["lr"]

        print(
            f"Epoch {epoch + 1:02d}/{EPOCHS} | "
            f"Train Loss: {training_loss:.4f} | "
            f"Val Loss: {validation_loss:.4f} | "
            f"Val Accuracy: {validation_accuracy:.2f}% | "
            f"LR: {current_lr:.6f}"
        )

        # --------------------------------------------------
        # Save best model
        # --------------------------------------------------

        if validation_loss < best_validation_loss:

            best_validation_loss = (
                validation_loss
            )

            epochs_without_improvement = 0

            torch.save(
                {
                    "model_state_dict":
                        model.state_dict(),

                    "vocab":
                        tokenizer.vocab,

                    "config":
                        {
                            "max_length":
                                MAX_LENGTH,

                            "d_model":
                                D_MODEL,

                            "num_heads":
                                NUM_HEADS,

                            "feed_forward_dimension":
                                FEED_FORWARD_DIMENSION,

                            "num_layers":
                                NUM_LAYERS,

                            "num_classes":
                                NUM_CLASSES,

                            "dropout":
                                DROPOUT
                        }
                },
                MODEL_PATH
            )

            print(
                "  → Best model saved."
            )

        else:

            epochs_without_improvement += 1

        # --------------------------------------------------
        # Early stopping
        # --------------------------------------------------

        if (
            epochs_without_improvement
            >= patience
        ):

            print(
                "\nEarly stopping."
            )

            break

    # --------------------------------------------------
    # Final test
    # --------------------------------------------------

    print("\n" + "=" * 60)
    print("FINAL TEST")
    print("=" * 60)

    checkpoint = torch.load(
        MODEL_PATH,
        map_location=device
    )

    model.load_state_dict(
        checkpoint[
            "model_state_dict"
        ]
    )

    (
        test_loss,
        test_accuracy,
        test_labels,
        test_predictions
    ) = evaluate(
        model,
        test_loader,
        device,
        loss_function
    )

    (
        precision,
        recall,
        f1,
        confusion_matrix
    ) = calculate_metrics(
        test_labels,
        test_predictions
    )

    print(
        "\nTest Loss:",
        f"{test_loss:.4f}"
    )

    print(
        "Test Accuracy:",
        f"{test_accuracy:.2f}%"
    )

    print(
        "Macro Precision:",
        f"{precision * 100:.2f}%"
    )

    print(
        "Macro Recall:",
        f"{recall * 100:.2f}%"
    )

    print(
        "Macro F1:",
        f"{f1 * 100:.2f}%"
    )

    print_confusion_matrix(
        confusion_matrix
    )

    print(
        "\nQuality Classes:"
    )

    print(
        "0 = Incorrect"
    )

    print(
        "1 = Weak"
    )

    print(
        "2 = Partially correct"
    )

    print(
        "3 = Good"
    )

    print(
        "4 = Excellent"
    )

    print(
        "\nModel saved to:",
        MODEL_PATH
    )


if __name__ == "__main__":

    main()
