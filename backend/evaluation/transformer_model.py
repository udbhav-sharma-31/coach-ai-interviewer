import math

import torch
import torch.nn as nn


class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_length=64):
        super().__init__()

        position = torch.arange(
            max_length,
            dtype=torch.float
        ).unsqueeze(1)

        div_term = torch.exp(
            torch.arange(0, d_model, 2).float()
            * (-math.log(10000.0) / d_model)
        )

        encoding = torch.zeros(
            max_length,
            d_model
        )

        encoding[:, 0::2] = torch.sin(
            position * div_term
        )

        encoding[:, 1::2] = torch.cos(
            position * div_term
        )

        self.register_buffer(
            "encoding",
            encoding.unsqueeze(0)
        )

    def forward(self, x):
        sequence_length = x.size(1)

        return x + self.encoding[:, :sequence_length, :]


class SelfAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()

        if d_model % num_heads != 0:
            raise ValueError(
                "d_model must be divisible by num_heads"
            )

        self.d_model = d_model
        self.num_heads = num_heads
        self.head_dimension = d_model // num_heads

        self.query = nn.Linear(d_model, d_model)
        self.key = nn.Linear(d_model, d_model)
        self.value = nn.Linear(d_model, d_model)

        self.output = nn.Linear(d_model, d_model)

    def forward(self, x, padding_mask=None):

        batch_size, sequence_length, _ = x.shape

        q = self.query(x)
        k = self.key(x)
        v = self.value(x)

        q = q.view(
            batch_size,
            sequence_length,
            self.num_heads,
            self.head_dimension
        ).transpose(1, 2)

        k = k.view(
            batch_size,
            sequence_length,
            self.num_heads,
            self.head_dimension
        ).transpose(1, 2)

        v = v.view(
            batch_size,
            sequence_length,
            self.num_heads,
            self.head_dimension
        ).transpose(1, 2)

        attention_scores = torch.matmul(
            q,
            k.transpose(-2, -1)
        )

        attention_scores = attention_scores / math.sqrt(
            self.head_dimension
        )

        if padding_mask is not None:

            mask = padding_mask.unsqueeze(1).unsqueeze(2)

            attention_scores = attention_scores.masked_fill(
                mask,
                float("-inf")
            )

        attention_weights = torch.softmax(
            attention_scores,
            dim=-1
        )

        attended = torch.matmul(
            attention_weights,
            v
        )

        attended = attended.transpose(1, 2).contiguous()

        attended = attended.view(
            batch_size,
            sequence_length,
            self.d_model
        )

        return self.output(attended)


class TransformerBlock(nn.Module):
    def __init__(
        self,
        d_model,
        num_heads,
        feed_forward_dimension,
        dropout=0.1
    ):
        super().__init__()

        self.attention = SelfAttention(
            d_model,
            num_heads
        )

        self.norm1 = nn.LayerNorm(d_model)

        self.feed_forward = nn.Sequential(
            nn.Linear(
                d_model,
                feed_forward_dimension
            ),
            nn.ReLU(),
            nn.Linear(
                feed_forward_dimension,
                d_model
            )
        )

        self.norm2 = nn.LayerNorm(d_model)

        self.dropout = nn.Dropout(dropout)

    def forward(self, x, padding_mask=None):

        attention_output = self.attention(
            x,
            padding_mask
        )

        x = self.norm1(
            x + self.dropout(attention_output)
        )

        feed_forward_output = self.feed_forward(x)

        x = self.norm2(
            x + self.dropout(feed_forward_output)
        )

        return x


class InterviewTransformer(nn.Module):

    def __init__(
        self,
        vocab_size,
        num_classes=5,
        max_length=128,
        d_model=128,
        num_heads=4,
        feed_forward_dimension=256,
        num_layers=2,
        dropout=0.1
    ):
        super().__init__()

        self.embedding = nn.Embedding(
            vocab_size,
            d_model,
            padding_idx=0
        )

        self.position = PositionalEncoding(
            d_model,
            max_length
        )

        self.transformer_layers = nn.ModuleList(
            [
                TransformerBlock(
                    d_model=d_model,
                    num_heads=num_heads,
                    feed_forward_dimension=feed_forward_dimension,
                    dropout=dropout
                )
                for _ in range(num_layers)
            ]
        )

        self.classifier = nn.Linear(
            d_model,
            num_classes
        )

    def forward(self, input_ids):

        padding_mask = input_ids == 0

        x = self.embedding(input_ids)

        x = self.position(x)

        for layer in self.transformer_layers:

            x = layer(
                x,
                padding_mask
            )

        # Ignore padding tokens during pooling.
        valid_tokens = (~padding_mask).unsqueeze(-1)

        x = x * valid_tokens

        token_count = valid_tokens.sum(
            dim=1
        ).clamp(min=1)

        x = x.sum(dim=1) / token_count

        logits = self.classifier(x)

        return logits


if __name__ == "__main__":

    model = InterviewTransformer(
        vocab_size=277
    )

    sample_input = torch.randint(
        0,
        277,
        (2, 128)
    )

    output = model(sample_input)

    print("Transformer created successfully!")

    print("Input shape:")
    print(sample_input.shape)

    print("Output shape:")
    print(output.shape)

    print("\nOutput:")
    print(output)