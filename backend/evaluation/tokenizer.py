import json
import re
from collections import Counter


# Special tokens
PAD_TOKEN = "<pad>"
UNK_TOKEN = "<unk>"
SEP_TOKEN = "<sep>"

# Maximum sequence length used by the Transformer
MAX_LENGTH = 128


class InterviewTokenizer:

    def __init__(self, min_frequency=1):

        self.min_frequency = min_frequency

        self.vocab = {
            PAD_TOKEN: 0,
            UNK_TOKEN: 1,
            SEP_TOKEN: 2,
        }

        self.inverse_vocab = {
            0: PAD_TOKEN,
            1: UNK_TOKEN,
            2: SEP_TOKEN,
        }

    def tokenize(self, text):
        """
        Convert text into tokens.

        Special token <sep> is preserved as a single token.
        """

        text = text.lower()

        tokens = re.findall(
            r"<sep>|\w+|[^\w\s]",
            text
        )

        return tokens

    def build_vocab(self, texts):
        """
        Build vocabulary from training texts.
        """

        counter = Counter()

        for text in texts:

            tokens = self.tokenize(text)

            counter.update(tokens)

        for token, frequency in counter.items():

            if frequency >= self.min_frequency:

                if token not in self.vocab:

                    index = len(self.vocab)

                    self.vocab[token] = index

                    self.inverse_vocab[index] = token

    def build_vocab_from_dataset(self, dataset):
        """
        Build vocabulary from question-answer pairs.

        Format:

        question <sep> answer
        """

        texts = []

        for item in dataset:

            text = (
                item["question"]
                + " "
                + SEP_TOKEN
                + " "
                + item["answer"]
            )

            texts.append(text)

        self.build_vocab(texts)

    def encode(self, text, max_length=MAX_LENGTH):
        """
        Convert text into token IDs.

        The sequence is truncated or padded to max_length.
        """

        tokens = self.tokenize(text)

        token_ids = []

        for token in tokens:

            token_id = self.vocab.get(
                token,
                self.vocab[UNK_TOKEN]
            )

            token_ids.append(token_id)

        # Truncate
        token_ids = token_ids[:max_length]

        # Pad
        while len(token_ids) < max_length:

            token_ids.append(
                self.vocab[PAD_TOKEN]
            )

        return token_ids

    def encode_pair(
        self,
        question,
        answer,
        max_length=MAX_LENGTH
    ):
        """
        Encode a question and candidate answer.

        Format:

        question <sep> answer
        """

        text = (
            question
            + " "
            + SEP_TOKEN
            + " "
            + answer
        )

        return self.encode(
            text,
            max_length=max_length
        )

    def decode(self, token_ids):
        """
        Convert token IDs back into text.
        """

        tokens = []

        for token_id in token_ids:

            token = self.inverse_vocab.get(
                token_id,
                UNK_TOKEN
            )

            # Do not display padding tokens
            if token == PAD_TOKEN:
                continue

            tokens.append(token)

        return " ".join(tokens)

    def save(self, path):
        """
        Save vocabulary to a JSON file.
        """

        with open(path, "w") as file:

            json.dump(
                self.vocab,
                file,
                indent=4
            )

    def load(self, path):
        """
        Load vocabulary from a JSON file.
        """

        with open(path, "r") as file:

            self.vocab = json.load(file)

        self.inverse_vocab = {
            int(index): token
            for token, index in self.vocab.items()
        }


def load_dataset(path):
    """
    Load interview dataset from JSON.
    """

    with open(path, "r") as file:

        return json.load(file)


if __name__ == "__main__":

    dataset = load_dataset(
        "data/interview_answers.json"
    )

    tokenizer = InterviewTokenizer()

    # Build vocabulary using question-answer pairs.
    tokenizer.build_vocab_from_dataset(dataset)

    print("=" * 60)
    print("INTERVIEW TOKENIZER TEST")
    print("=" * 60)

    print("Dataset examples:", len(dataset))

    print("Vocabulary size:", len(tokenizer.vocab))

    print("\nSpecial tokens:")

    print("PAD:", PAD_TOKEN, "->", tokenizer.vocab[PAD_TOKEN])
    print("UNK:", UNK_TOKEN, "->", tokenizer.vocab[UNK_TOKEN])
    print("SEP:", SEP_TOKEN, "->", tokenizer.vocab[SEP_TOKEN])

    sample_question = (
        "What is inheritance in Python?"
    )

    sample_answer = (
        "Inheritance allows a class to reuse "
        "properties and methods from another class."
    )

    print("\nQuestion:")
    print(sample_question)

    print("\nAnswer:")
    print(sample_answer)

    combined = (
        sample_question
        + " "
        + SEP_TOKEN
        + " "
        + sample_answer
    )

    print("\nTokens:")
    print(tokenizer.tokenize(combined))

    encoded = tokenizer.encode_pair(
        sample_question,
        sample_answer
    )

    print("\nEncoded:")
    print(encoded)

    print("\nFirst 20 token IDs:")
    print(encoded[:20])

    print("\nDecoded:")
    print(tokenizer.decode(encoded))

    print("\nTokenizer test completed successfully!")
