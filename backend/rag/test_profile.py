from backend.rag.pdf_loader import extract_text_from_pdf
from backend.rag.profile_extractor import extract_resume_profile


PDF_PATH = "data/sample_resume.pdf"


def main():
    print("\n" + "=" * 60)
    print("RESUME PROFILE EXTRACTION TEST")
    print("=" * 60)

    resume_text = extract_text_from_pdf(PDF_PATH)

    profile = extract_resume_profile(resume_text)

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

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()