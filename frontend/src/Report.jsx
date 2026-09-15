import { useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import "./Report.css";
import CoachLogo from "./components/CoachLogo";
import { useAuth } from "./AuthContext";

function Report() {
  const navigate = useNavigate();
  const location = useLocation();
  const { user } = useAuth();
  const report = location.state?.report;
  useEffect(() => {
  if (!report || !user?.id) {
    return;
  }

  const historyKey =
    `coach_ai_interview_history_${user.id}`;

  const existingHistory = JSON.parse(
    localStorage.getItem(historyKey) || "[]"
  );

  const interviewId =
    report.sessionId || `interview-${Date.now()}`;

  const alreadySaved = existingHistory.some(
    (interview) => interview.id === interviewId
  );

  if (alreadySaved) {
    return;
  }

  const interview = {
    id: interviewId,
    role: report.role || "Interview",
    score: Number(report.overallScore || 0),
    difficulty: report.difficulty || "beginner",
    questionCount: report.questions?.length || 0,
    date: new Date().toISOString(),
  };

  const updatedHistory = [
    interview,
    ...existingHistory,
  ].slice(0, 20);

  localStorage.setItem(
    historyKey,
    JSON.stringify(updatedHistory)
  );
}, [report, user]);
  // Safety fallback if someone opens /report directly.
  if (!report) {
    return (
      <div className="report-page">
        <div className="report-glow report-glow-one"></div>
        <div className="report-glow report-glow-two"></div>

        <main className="report-content">
          <div className="report-intro">
            <span>NO REPORT FOUND</span>

            <h1>
              Start an
              <br />
              <strong>interview first.</strong>
            </h1>

            <p>
              Complete an interview to see your personalized
              performance report.
            </p>

            <button
              className="new-interview-btn"
              onClick={() => navigate("/setup")}
            >
              Start Interview
              <span>→</span>
            </button>
          </div>
        </main>
      </div>
    );
  }

  const {
    questions = [],
    answers = [],
    evaluations = [],
    overallScore = 0,
    difficulty = "beginner",
    finalReport = {},
  } = report;

  const score = Number(overallScore || 0);

  const getResultLabel = (evaluation) => {
    const evaluationScore = Number(evaluation.score || 0);

    if (evaluationScore >= 9) {
      return "Excellent";
    }

    if (evaluationScore >= 8) {
      return "Strong";
    }

    if (evaluationScore >= 6) {
      return "Good";
    }

    if (evaluationScore >= 4) {
      return "Needs Work";
    }

    return "Weak";
  };

  const getTopicLabel = (question, index) => {
    const text = (question || "").toLowerCase();

    if (
      text.includes("resume") ||
      text.includes("experience") ||
      text.includes("worked") ||
      text.includes("project") ||
      text.includes("client")
    ) {
      if (index < 2) {
        return "Resume Experience";
      }
    }

    if (
      text.includes("technical") ||
      text.includes("python") ||
      text.includes("java") ||
      text.includes("database") ||
      text.includes("sql") ||
      text.includes("api") ||
      text.includes("microservice") ||
      text.includes("architecture") ||
      text.includes("system design") ||
      text.includes("machine learning") ||
      text.includes("transformer") ||
      text.includes("llm") ||
      text.includes("rag")
    ) {
      return "Technical";
    }

    if (index === 2) {
      return "Transferable Skills";
    }

    if (index === 3) {
      return "Target Role";
    }

    return "Interview Question";
  };

  const evaluationsForDisplay = evaluations.map(
    (evaluation, index) => ({
      number: String(index + 1).padStart(2, "0"),
      topic: getTopicLabel(questions[index], index),
      score: Number(evaluation.score || 0).toFixed(1),
      result: getResultLabel(evaluation),
    })
  );

  const strongEvaluations = evaluations.filter(
    (evaluation) => Number(evaluation.score || 0) >= 8
  );

  const weakEvaluations = evaluations.filter(
    (evaluation) => Number(evaluation.score || 0) < 6
  );

  const strengthsText =
  finalReport.strengths ||
  (
    strongEvaluations.length > 0
      ? `You performed strongly on ${strongEvaluations.length} ${
          strongEvaluations.length === 1
            ? "question"
            : "questions"
        }. Your strongest responses demonstrated relevance, clarity, and a good understanding of the topics discussed.`
      : "Your responses provide a useful starting point. Continue practicing structured answers and focus on directly addressing what each question asks."
  );

const improvementText =
  finalReport.improvements ||
  (
    weakEvaluations.length > 0
      ? `${weakEvaluations.length} ${
          weakEvaluations.length === 1
            ? "response needs"
            : "responses need"
        } more development. Focus on giving specific examples, explaining your reasoning, and directly addressing the question before adding supporting details.`
      : "Keep improving by adding specific examples, explaining the actions you personally took, and including measurable outcomes whenever possible."
  );

  const getRecommendation = () => {
    if (score >= 8.5) {
      return {
        title: "Excellent interview performance.",
        description:
          "You demonstrated strong overall performance. Continue practicing advanced questions and focus on making your answers even more precise and impactful.",
      };
    }

    if (score >= 7) {
      return {
        title: "You're on the right track.",
        description:
          "Your overall performance was solid. Continue practicing structured answers and strengthen the areas where your scores were lower.",
      };
    }

    if (score >= 5) {
      return {
        title: "There's room to improve.",
        description:
          "Focus on understanding the question before answering, giving concrete examples, and explaining your reasoning more clearly.",
      };
    }

    return {
      title: "Keep practicing.",
      description:
        "Use each interview as practice. Focus on building confidence, understanding the questions, and giving complete, relevant answers.",
    };
  };
const recommendation = getRecommendation();
  const finalRecommendation = {
  title: recommendation.title,
  description:
    finalReport.recommendation ||
    recommendation.description,
  };

  return (
    <div className="report-page">

      <div className="report-glow report-glow-one"></div>
      <div className="report-glow report-glow-two"></div>

      {/* Header */}

      <header className="report-header">

        <button
          className="report-logo"
          onClick={() => navigate("/home")}
        >
          <div className="report-brand">
  <CoachLogo size="sm" />
</div>
          <span>COACH AI</span>
        </button>

        <div className="report-header-title">
          INTERVIEW REPORT
        </div>

        <button
          className="new-interview-btn"
          onClick={() => navigate("/setup")}
        >
          New Interview
          <span>↗</span>
        </button>

      </header>

      {/* Main */}

      <main className="report-content">

        <div className="report-intro">

          <span>INTERVIEW COMPLETE</span>

          <h1>
            Here's how you
            <br />
            <strong>performed.</strong>
          </h1>

          <p>
            Coach AI analyzed your responses and prepared
            a personalized performance report.
          </p>

        </div>

        {/* Score */}

        <section className="score-section">

          <div className="score-card">

            <div className="score-orb">
              <div className="score-orb-core">
                ✦
              </div>
            </div>

            <div className="score-info">

              <span>OVERALL SCORE</span>

              <div className="score-number">
                {score.toFixed(1)}
                <small>/10</small>
              </div>

              <p>
                {score >= 8
                  ? "Strong performance"
                  : score >= 6
                  ? "Good performance"
                  : "Needs improvement"}
              </p>

            </div>

          </div>

          <div className="score-summary">

            <div>
              <span>QUESTIONS</span>
              <strong>
                {String(questions.length).padStart(2, "0")}
              </strong>
            </div>

            <div>
              <span>AVERAGE</span>
              <strong>
                {score.toFixed(1)}/10
              </strong>
            </div>

            <div>
              <span>LEVEL</span>
              <strong>
                {difficulty.charAt(0).toUpperCase() +
                  difficulty.slice(1)}
              </strong>
            </div>

          </div>

        </section>

        {/* Evaluation breakdown */}

        <section className="breakdown-section">

          <div className="section-heading">

            <div>
              <span>PERFORMANCE</span>

              <h2>
                Question breakdown
              </h2>
            </div>

            <p>
              Your performance across the interview.
            </p>

          </div>

          <div className="evaluation-list">

            {evaluationsForDisplay.map(
              (evaluation) => (

                <div
                  className="evaluation-row"
                  key={evaluation.number}
                >

                  <div className="evaluation-number">
                    {evaluation.number}
                  </div>

                  <div className="evaluation-topic">

                    <span>
                      {evaluation.topic}
                    </span>

                    <strong>
                      {evaluation.result}
                    </strong>

                  </div>

                  <div className="evaluation-score">
                    {evaluation.score}
                    <small>/10</small>
                  </div>

                </div>

              )
            )}

          </div>

        </section>

        {/* Feedback */}

        <section className="feedback-grid">

          <div className="feedback-card">

            <span>
              01 — STRENGTHS
            </span>

            <h3>
              What you did well
            </h3>

            <p>
              {strengthsText}
            </p>

          </div>

          <div className="feedback-card">

            <span>
              02 — IMPROVEMENT
            </span>

            <h3>
              Where to improve
            </h3>

            <p>
              {improvementText}
            </p>

          </div>

        </section>

        {/* Final recommendation */}

        <section className="recommendation-card">

          <div>

            <span>
              COACH AI RECOMMENDATION
            </span>

            <h2>
              {finalRecommendation.title}
            </h2>

            <p>
              {finalRecommendation.description}
            </p>

          </div>

          <button
            onClick={() => navigate("/setup")}
          >
            Practice Again
            <span>→</span>
          </button>

        </section>

      </main>

    </div>
  );
}

export default Report;