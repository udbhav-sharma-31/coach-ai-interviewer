from langgraph.types import interrupt


def answer_node(state):
    answer = interrupt("Waiting for candidate's answer...")

    return {
        "current_answer": answer,
    }