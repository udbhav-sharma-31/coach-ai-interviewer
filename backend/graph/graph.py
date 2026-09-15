from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from backend.graph.state import InterviewGraphState
from backend.graph.question_node import generate_question
from backend.graph.answer_node import answer_node
from backend.graph.evaluation_node import evaluate_node
from backend.graph.difficulty_node import difficulty_node
from backend.graph.resume_node import resume_node
from backend.graph.final_report_node import final_report_node

def should_continue(state):

    if state["question_number"] >= state["max_questions"]:
        return "end"

    return "continue"


graph_builder = StateGraph(InterviewGraphState)


# ---------------------------------------------------------
# Nodes
# ---------------------------------------------------------

graph_builder.add_node(
    "resume",
    resume_node,
)

graph_builder.add_node(
    "generate_question",
    generate_question,
)

graph_builder.add_node(
    "answer",
    answer_node,
)

graph_builder.add_node(
    "evaluate_answer",
    evaluate_node,
)

graph_builder.add_node(
    "difficulty",
    difficulty_node,
)
graph_builder.add_node("final_report", final_report_node)

# ---------------------------------------------------------
# Initial interview flow
# ---------------------------------------------------------

graph_builder.add_edge(
    START,
    "resume",
)

graph_builder.add_edge(
    "resume",
    "generate_question",
)

graph_builder.add_edge(
    "generate_question",
    "answer",
)

graph_builder.add_edge(
    "answer",
    "evaluate_answer",
)

graph_builder.add_edge(
    "evaluate_answer",
    "difficulty",
)


# ---------------------------------------------------------
# Continue or finish
# ---------------------------------------------------------

graph_builder.add_conditional_edges(
    "difficulty",
    should_continue,
    {
        "continue": "generate_question",
        "end": "final_report",
    },
)

graph_builder.add_edge("final_report", END)


# ---------------------------------------------------------
# Memory
# ---------------------------------------------------------

memory = MemorySaver()

interview_graph = graph_builder.compile(
    checkpointer=memory,
)