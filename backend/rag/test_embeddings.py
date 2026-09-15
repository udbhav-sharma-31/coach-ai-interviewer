from backend.rag.pdf_loader import extract_text_from_pdf
from backend.rag.chunker import chunk_text
from backend.rag.embeddings import ResumeEmbedder


pdf_path = "data/sample_resume.pdf"

text = extract_text_from_pdf(pdf_path)

chunks = chunk_text(text)

embedder = ResumeEmbedder()

embeddings = embedder.embed(chunks)

print("\n" + "=" * 60)
print("EMBEDDING TEST")
print("=" * 60)

print("Number of chunks:", len(chunks))
print("Embedding shape:", embeddings.shape)
print("Embedding dimension:", embeddings.shape[1])

print("\nFirst embedding:")
print(embeddings[0])

print("\n" + "=" * 60)