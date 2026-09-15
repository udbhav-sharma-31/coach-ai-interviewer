from backend.rag.resume_rag import ResumeRAG


def get_resume_context(
    resume_available: bool,
    resume_rag: ResumeRAG | None,
    query: str,
    top_k: int = 3,
) -> str:
    """
    Retrieve resume information when a resume is available.

    If no resume was provided, return an empty context.
    """

    if not resume_available:
        return ""

    if resume_rag is None:
        return ""

    return resume_rag.get_context(
        query,
        top_k=top_k,
    )