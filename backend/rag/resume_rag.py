from backend.rag.pdf_loader import extract_text_from_pdf
from backend.rag.chunker import chunk_resume
from backend.rag.embeddings import ResumeEmbedder
from backend.rag.vector_store import ResumeVectorStore


class ResumeRAG:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

        # Extract resume text
        text = extract_text_from_pdf(pdf_path)

        # Split resume into chunks
        self.chunks = chunk_resume(text)

        if not self.chunks:
            raise ValueError("No text could be extracted from the resume.")

        # Create embeddings
        self.embedder = ResumeEmbedder()
        embeddings = self.embedder.embed(self.chunks)

        # Create FAISS vector store
        self.vector_store = ResumeVectorStore(
            dimension=embeddings.shape[1]
        )

        # Add resume chunks to FAISS
        self.vector_store.add(
            embeddings,
            self.chunks,
        )

    def retrieve(self, query: str, top_k: int = 3):
        """
        Retrieve the most relevant resume chunks for a query.
        """

        query_embedding = self.embedder.embed([query])

        return self.vector_store.search(
            query_embedding,
            top_k=top_k,
        )

    def get_context(self, query: str, top_k: int = 3):
        """
        Return retrieved resume chunks as a single text context.
        """

        results = self.retrieve(query, top_k)

        if not results:
            return ""

        return "\n\n".join(
            result["chunk"]
            for result in results
        )