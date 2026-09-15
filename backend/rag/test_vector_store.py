from backend.rag.pdf_loader import extract_text_from_pdf
from backend.rag.chunker import chunk_text
from backend.rag.embeddings import ResumeEmbedder
from backend.rag.vector_store import ResumeVectorStore


pdf_path = "data/sample_resume.pdf"

text = extract_text_from_pdf(pdf_path)

chunks = chunk_text(text)

embedder = ResumeEmbedder()

embeddings = embedder.embed(chunks)

vector_store = ResumeVectorStore(
    dimension=embeddings.shape[1]
)

vector_store.add(
    embeddings,
    chunks,
)


query = "What experience does the candidate have working with children?"

query_embedding = embedder.embed([query])

results = vector_store.search(
    query_embedding,
    top_k=3,
)

print("\n" + "=" * 60)
print("RESUME VECTOR SEARCH TEST")
print("=" * 60)

print("Query:")
print(query)

print("\nResults:")

for i, result in enumerate(results):
    print(f"\n--- RESULT {i + 1} ---")
    print(f"Similarity: {result['score']:.4f}")
    print(result["chunk"])

print("\n" + "=" * 60)