from backend.rag.resume_rag import ResumeRAG
from backend.llm.local_client import ask_local_llm
from backend.llm.prompts import INTERVIEWER_SYSTEM_PROMPT


# Load the candidate's resume into the RAG system
rag = ResumeRAG("data/sample_resume.pdf")


# Query the resume
query = "What experience does the candidate have working with children?"

# Retrieve relevant resume information
context = rag.get_context(query, top_k=3)


# Give the retrieved resume context to Qwen
prompt = f"""
You are conducting an interview.

Candidate resume context:
{context}

Interview role:
Python Developer

Experience level:
Beginner

Skills:
Python, Machine Learning, Generative AI

Using the candidate's resume context, generate ONE personalized
interview question.

The question should connect the candidate's background to the
interview role or skills.

Return ONLY the question.
Do not explain your choice.
Do not show reasoning.
Do not provide the answer.
"""


question = ask_local_llm(
    prompt,
    system_prompt=INTERVIEWER_SYSTEM_PROMPT,
)


print("\n" + "=" * 60)
print("RAG + QWEN TEST")
print("=" * 60)

print("\nRetrieved Resume Context:")
print(context)

print("\nGenerated Personalized Question:")
print(question)

print("\n" + "=" * 60)