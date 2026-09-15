import os

import torch

from backend.evaluation.tokenizer import InterviewTokenizer
from backend.evaluation.transformer_model import InterviewTransformer


MODEL_PATH = "models/interview_evaluator.pt"


class InterviewEvaluator:
    """
    Loads the trained custom Transformer and evaluates
    a candidate's answer to an interview question.
    """

    LABEL_NAMES = {
        0: "Incorrect",
        1: "Weak",
        2: "Partially Correct",
        3: "Good",
        4: "Excellent",
    }

    def __init__(self):

        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(
                f"Model not found: {MODEL_PATH}"
            )

        checkpoint = torch.load(
            MODEL_PATH,
            map_location="cpu",
            weights_only=False,
        )

        self.device = torch.device(
            "mps"
            if torch.backends.mps.is_available()
            else "cpu"
        )

        # Load vocabulary directly from checkpoint
        self.tokenizer = InterviewTokenizer()

        self.tokenizer.vocab = checkpoint["vocab"]

        self.tokenizer.inverse_vocab = {
            int(index): token
            for token, index in self.tokenizer.vocab.items()
        }

        self.model = InterviewTransformer(
            vocab_size=len(self.tokenizer.vocab),
            num_classes=5,
            max_length=128,
            d_model=160,
            num_heads=4,
            feed_forward_dimension=512,
            num_layers=3,
            dropout=0.2,
        )

        self.model.load_state_dict(
            checkpoint["model_state_dict"]
        )

        self.model.to(self.device)

        self.model.eval()

    def evaluate(self, question, answer):

        token_ids = self.tokenizer.encode_pair(
            question,
            answer,
            max_length=128,
        )

        input_tensor = torch.tensor(
            [token_ids],
            dtype=torch.long,
            device=self.device,
        )

        with torch.no_grad():

            logits = self.model(input_tensor)

            probabilities = torch.softmax(
                logits,
                dim=-1,
            )

            prediction = torch.argmax(
                probabilities,
                dim=-1,
            ).item()

            confidence = probabilities[
                0, prediction
            ].item()

        return {
            "label": prediction,
            "quality": self.LABEL_NAMES[prediction],
            "score": prediction * 2 + 2,
            "confidence": round(confidence, 4),
        }


if __name__ == "__main__":

    evaluator = InterviewEvaluator()

    question = "What is overfitting in machine learning?"

    answers = [
        "Overfitting means the model performs well on every dataset.",
        "Overfitting happens when a model learns the training data too closely.",
        "Overfitting occurs when a model learns training examples and noise too closely, reducing its ability to generalize.",
        "Overfitting occurs when a model memorizes training-specific patterns and noise instead of learning patterns that generalize to unseen data. It can often be reduced using regularization, dropout, more diverse data, or early stopping.",
    ]

    print("=" * 60)
    print("CUSTOM TRANSFORMER INFERENCE TEST")
    print("=" * 60)

    for answer in answers:

        result = evaluator.evaluate(
            question,
            answer,
        )

        print()
        print("Question:", question)
        print("Answer:", answer)
        print("Result:", result)