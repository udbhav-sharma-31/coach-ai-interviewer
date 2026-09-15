from backend.evaluation.final_report import generate_final_report


def final_report_node(state):

    final_report = generate_final_report(
        questions=state["questions"],
        answers=state["answers"],
        evaluations=state["evaluations"],
    )

    print("\n" + "=" * 60)
    print("FINAL QWEN REPORT")
    print("=" * 60)

    print("\nStrengths:")
    print(final_report["strengths"])

    print("\nImprovements:")
    print(final_report["improvements"])

    print("\nRecommendation:")
    print(final_report["recommendation"])

    print("=" * 60)

    return {
        "final_report": final_report,
    }