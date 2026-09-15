import faiss
import numpy as np


class ResumeVectorStore:
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatIP(dimension)
        self.chunks = []

    def add(self, embeddings, chunks: list[str]):
        embeddings = np.asarray(embeddings, dtype="float32")

        self.index.add(embeddings)
        self.chunks.extend(chunks)

    def search(self, query_embedding, top_k: int = 3):
        query_embedding = np.asarray(
            query_embedding,
            dtype="float32",
        )

        scores, indices = self.index.search(
            query_embedding,
            min(top_k, len(self.chunks)),
        )

        results = []

        for score, index in zip(scores[0], indices[0]):
            if index == -1:
                continue

            results.append(
                {
                    "chunk": self.chunks[index],
                    "score": float(score),
                }
            )

        return results