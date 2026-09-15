from backend.rag.pdf_loader import extract_text_from_pdf
from backend.rag.profile_extractor import extract_resume_profile



def resume_node(state):
    """
    Load the candidate resume and create a grounded profile.

    The target role comes from the candidate information.
    Resume information comes only from the resume itself.
    """

    if not state["resume_available"]:
        return {
            "resume_profile": {
                "education": [],
                "experience": [],
                "skills": [],
                "domains": [],
                "projects": [],
                "certifications": [],
            },
            "resume_context": "",
        }

    resume_text = extract_text_from_pdf(state["resume_path"])

    profile = extract_resume_profile(resume_text)

    resume_profile = {
        "education": profile.education,
        "experience": profile.experience,
        "skills": profile.skills,
        "domains": profile.domains,
        "projects": profile.projects,
        "certifications": profile.certifications,
    }

    print("\n" + "=" * 60)
    print("RESUME PROFILE")
    print("=" * 60)

    print(f"\nTarget Role: {state['target_role']}")

    print("\nEducation:")
    for item in profile.education:
        print(f"- {item}")

    print("\nExperience:")
    for item in profile.experience:
        print(f"- {item}")

    print("\nSkills:")
    for item in profile.skills:
        print(f"- {item}")

    print("\nDomains:")
    for item in profile.domains:
        print(f"- {item}")

    print("\nProjects:")
    for item in profile.projects:
        print(f"- {item}")

    print("\nCertifications:")
    for item in profile.certifications:
        print(f"- {item}")

    print("=" * 60)

    return {
        "resume_profile": resume_profile,
        "resume_context": resume_text,
    }