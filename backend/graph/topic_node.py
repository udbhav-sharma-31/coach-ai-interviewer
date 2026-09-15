from backend.llm.local_client import ask_local_llm_json


def extract_question_topic(question: str) -> str:
    """
    Identify the main technical topic of an interview question.
    """

    prompt = f"""
Identify the main technical topic of this interview question.

Question:
{question}

Return ONE short topic name.

Examples:
- Python modules
- garbage collection
- exception handling
- decorators
- REST APIs
- SQL databases
- machine learning
- transformers
- RAG

Do not explain.

Return exactly:

{{
    "topic": "topic name"
}}
"""

    schema = {
        "type": "object",
        "properties": {
            "topic": {
                "type": "string"
            }
        },
        "required": [
            "topic"
        ]
    }

    data = ask_local_llm_json(
        prompt,
        schema=schema,
    )

    return data["topic"].strip().lower()


def topic_node(state):

    question = state["current_question"]

    topic = extract_question_topic(question)

    covered_topics = list(state["covered_topics"])

    if topic not in covered_topics:
        covered_topics.append(topic)

    print("\nTOPIC TRACKING")
    print("-" * 60)
    print(f"Current topic: {topic}")
    print(f"Covered topics: {covered_topics}")
    print("-" * 60)

    return {
        "covered_topics": covered_topics
    }