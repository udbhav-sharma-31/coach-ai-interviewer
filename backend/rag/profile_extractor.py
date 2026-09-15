import re

from backend.rag.resume_profile import ResumeProfile


def _clean_lines(text: str) -> list[str]:
    """Return meaningful cleaned lines from resume text."""

    lines = []

    for line in text.splitlines():
        line = line.strip()

        if not line:
            continue

        line = re.sub(r"\s+", " ", line)

        lines.append(line)

    return lines


def _section_lines(text: str, headings: list[str]) -> list[str]:
    """
    Extract lines belonging to one of the requested resume sections.
    """

    lines = _clean_lines(text)

    heading_pattern = re.compile(
        r"^(?:" + "|".join(headings) + r")$",
        re.IGNORECASE,
    )

    section = []
    collecting = False

    known_headings = re.compile(
        r"^(career summary|professional summary|summary|"
        r"objective|skills|technical skills|experience|"
        r"work experience|employment history|education|"
        r"projects|certifications|achievements|"
        r"responsibilities|internships|childcare|"
        r"adult care)$",
        re.IGNORECASE,
    )

    for line in lines:

        if heading_pattern.match(line):
            collecting = True
            continue

        if collecting and known_headings.match(line):
            break

        if collecting:
            section.append(line)

    return section


def _contains_any(text: str, keywords: list[str]) -> bool:
    text_lower = text.lower()
    return any(keyword.lower() in text_lower for keyword in keywords)


def extract_resume_profile(resume_context: str) -> ResumeProfile:
    """
    Build a grounded resume profile directly from resume text.

    This intentionally does not use an LLM.
    Information is copied or summarized only from text that
    actually appears in the resume.
    """

    if not resume_context or not resume_context.strip():
        return ResumeProfile()

    lines = _clean_lines(resume_context)

    education = []
    experience = []
    skills = []
    domains = []
    projects = []
    certifications = []

    # ---------------------------------------------------------
    # EDUCATION
    # ---------------------------------------------------------

    education_keywords = [
        "BS ",
        "BA ",
        "B.S.",
        "B.A.",
        "Bachelor",
        "Master",
        "M.S.",
        "M.A.",
        "PhD",
        "GPA",
        "Dean's List",
        "Chancellor's List",
    ]

    for line in lines:
        if _contains_any(line, education_keywords):
            education.append(line)

    # ---------------------------------------------------------
    # EXPERIENCE
    # ---------------------------------------------------------

    experience_keywords = [
        "Supervisor",
        "Specialist",
        "Teacher",
        "Manager",
        "Director",
        "Assistant",
        "Coordinator",
        "Counselor",
    ]

    for line in lines:
        if _contains_any(line, experience_keywords):
            experience.append(line)

    # ---------------------------------------------------------
    # SKILLS / RESPONSIBILITIES
    # ---------------------------------------------------------

    skill_keywords = [
        "maintained",
        "managed",
        "coordinated",
        "oversaw",
        "assisted",
        "determined",
        "planning",
        "researching",
        "records",
        "databases",
        "client",
        "volunteer",
    ]

    for line in lines:
        if _contains_any(line, skill_keywords):
            skills.append(line)

    # ---------------------------------------------------------
    # DOMAINS
    # ---------------------------------------------------------

    domain_keywords = {
        "early childhood development": [
            "early childhood",
            "childcare",
            "children",
        ],
        "elementary education": [
            "elementary education",
            "teacher",
            "classroom",
            "student",
        ],
        "special-needs care": [
            "special needs",
        ],
        "counseling": [
            "counseling",
            "counselor",
        ],
        "client management": [
            "client",
            "client databases",
            "client records",
        ],
        "volunteer management": [
            "volunteer",
        ],
    }

    combined_text = " ".join(lines).lower()

    for domain, keywords in domain_keywords.items():
        if any(keyword in combined_text for keyword in keywords):
            domains.append(domain)

    # ---------------------------------------------------------
    # PROJECTS
    # ---------------------------------------------------------

    project_heading_lines = _section_lines(
        resume_context,
        [
            "projects",
        ],
    )

    projects.extend(project_heading_lines)

    # ---------------------------------------------------------
    # CERTIFICATIONS
    # ---------------------------------------------------------

    certification_heading_lines = _section_lines(
        resume_context,
        [
            "certifications",
        ],
    )

    certifications.extend(certification_heading_lines)

    # Remove duplicates while preserving order.
    education = list(dict.fromkeys(education))
    experience = list(dict.fromkeys(experience))
    skills = list(dict.fromkeys(skills))
    domains = list(dict.fromkeys(domains))
    projects = list(dict.fromkeys(projects))
    certifications = list(dict.fromkeys(certifications))

    return ResumeProfile(
        education=education,
        experience=experience,
        skills=skills,
        domains=domains,
        projects=projects,
        certifications=certifications,
    )