from backend.rag.pdf_loader import extract_text_from_pdf
from backend.rag.chunker import chunk_text


pdf_path = "data/sample_resume.pdf"

text = extract_text_from_pdf(pdf_path)

chunks = chunk_text(text)

print("\n" + "=" * 60)
print("RESUME CHUNKING TEST")
print("=" * 60)

print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\n--- CHUNK {i + 1} ---")
    print(chunk)

print("\n" + "=" * 60)