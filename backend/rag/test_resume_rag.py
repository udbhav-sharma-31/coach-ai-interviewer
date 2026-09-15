from backend.rag.resume_rag import ResumeRAG


rag = ResumeRAG("data/sample_resume.pdf")


query = "What experience does the candidate have working with children?"

context = rag.get_context(query)


print("\n" + "=" * 60)
print("RESUME RAG TEST")
print("=" * 60)

print("\nQuery:")
print(query)

print("\nRetrieved Context:")
print(context)

print("\n" + "=" * 60)