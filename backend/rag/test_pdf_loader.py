from backend.rag.pdf_loader import extract_text_from_pdf


pdf_path = "data/sample_resume.pdf"

text = extract_text_from_pdf(pdf_path)

print("\n" + "=" * 60)
print("EXTRACTED RESUME TEXT")
print("=" * 60)

print(text)

print("\n" + "=" * 60)
print("CHARACTERS EXTRACTED:", len(text))
print("=" * 60)