import re


def chunk_resume(text: str) -> list[str]:
    """
    Split a resume into meaningful sections.

    The goal is to preserve resume structure instead of creating
    one large generic text chunk.
    """

    if not text or not text.strip():
        return []

    # Normalize whitespace while preserving section boundaries.
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # Common resume section headings.
    heading_pattern = re.compile(
        r"(?i)"
        r"(career summary|professional summary|summary|"
        r"objective|"
        r"skills|technical skills|"
        r"experience|work experience|employment history|"
        r"education|"
        r"projects|"
        r"certifications|"
        r"achievements|"
        r"responsibilities|"
        r"internships)"
    )

    matches = list(heading_pattern.finditer(text))

    chunks = []

    # If no recognizable headings are found, fall back to paragraph chunks.
    if not matches:
        paragraphs = [
            paragraph.strip()
            for paragraph in text.split("\n\n")
            if paragraph.strip()
        ]

        return paragraphs

    # Text before the first recognized heading.
    if matches[0].start() > 0:
        intro = text[:matches[0].start()].strip()
        if intro:
            chunks.append(intro)

    for index, match in enumerate(matches):
        heading = match.group(1).strip()

        start = match.start()
        end = (
            matches[index + 1].start()
            if index + 1 < len(matches)
            else len(text)
        )

        section_text = text[start:end].strip()

        if section_text:
            chunks.append(section_text)

    return chunks


# Keep the old function name available so existing code does not break.
def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """
    Backward-compatible wrapper.

    Resume documents should use chunk_resume().
    """

    return chunk_resume(text)