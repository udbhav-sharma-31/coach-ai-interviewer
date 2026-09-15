from backend.interview.state import InterviewState


interview_sessions: dict[str, InterviewState] = {}


def save_interview(session_id: str, state: InterviewState):
    interview_sessions[session_id] = state


def get_interview(session_id: str) -> InterviewState:
    if session_id not in interview_sessions:
        raise ValueError("Interview session not found")

    return interview_sessions[session_id]