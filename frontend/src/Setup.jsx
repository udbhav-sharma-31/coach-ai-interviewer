import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Setup.css";
import CoachLogo from "./components/CoachLogo";

function Setup() {
  const navigate = useNavigate();

  const [resume, setResume] = useState(null);
  const [role, setRole] = useState("");
  const [experienceLevel, setExperienceLevel] = useState("Beginner");
  const [skills, setSkills] = useState("");

  const handleResumeChange = (event) => {
    const file = event.target.files[0];

    if (file && file.type === "application/pdf") {
      setResume(file);
    }
  };

  const handleStartInterview = async () => {
  if (!resume || !role.trim()) {
    return;
  }

  try {
    const formData = new FormData();

    formData.append("name", "Udbhav");
    formData.append("role", role);
    formData.append("experience_level", experienceLevel);
    formData.append("skills", skills);
    formData.append("resume", resume);

    const response = await fetch(
      "http://127.0.0.1:8000/interview/start",
      {
        method: "POST",
        body: formData,
      }
    );

    const data = await response.json();

    if (!response.ok) {
      console.error("Interview start failed:", data);
      return;
    }

    console.log("Interview started:", data);

    navigate("/interview", {
      state: {
        sessionId: data.session_id,
        question: data.question,
        questionNumber: data.question_number,
        difficulty: data.difficulty,
        role: role,
      },
    });

  } catch (error) {
    console.error("Could not connect to backend:", error);
  }
};

  return (
    <div className="setup-page">

      <div className="setup-glow setup-glow-one"></div>
      <div className="setup-glow setup-glow-two"></div>

      {/* Header */}
      <header className="setup-header">

        <button
          className="setup-logo"
          onClick={() => navigate("/home")}
        >
          <div className="setup-brand">
  <CoachLogo size="sm" />
</div>
          <div className="logo-text">COACH AI</div>
        </button>

        <div className="setup-progress">
          <span className="progress-active">01</span>
          <span>Setup Interview</span>
        </div>

        <button
          className="back-home"
          onClick={() => navigate("/home")}
        >
          ← Dashboard
        </button>

      </header>


      {/* Main */}
      <main className="setup-content">

        <div className="setup-title">
          <span>✦ INTERVIEW CONFIGURATION</span>

          <h1>
            Let's prepare your
            <br />
            <strong>interview.</strong>
          </h1>

          <p>
            Tell Coach AI about the interview you want to practice.
            We'll use your resume to personalize the experience.
          </p>
        </div>


        <div className="setup-layout">

          {/* Left column */}
          <div className="setup-main-card">

            {/* Resume */}
            <section className="setup-section">

              <div className="setup-section-heading">
                <div className="section-icon">01</div>

                <div>
                  <h2>Upload your resume</h2>
                  <p>We'll use it to create resume-aware questions.</p>
                </div>
              </div>

              <label
                className={`resume-dropzone ${
                  resume ? "resume-selected" : ""
                }`}
              >

                <input
                  type="file"
                  accept=".pdf,application/pdf"
                  onChange={handleResumeChange}
                />

                <div className="upload-icon">
                  {resume ? "✓" : "↑"}
                </div>

                {resume ? (
                  <>
                    <strong>{resume.name}</strong>
                    <span>
                      {(resume.size / 1024 / 1024).toFixed(2)} MB · PDF
                    </span>
                  </>
                ) : (
                  <>
                    <strong>Drop your resume here</strong>
                    <span>or click to browse · PDF only</span>
                  </>
                )}

              </label>

            </section>


            {/* Target role */}
            <section className="setup-section">

              <div className="setup-section-heading">
                <div className="section-icon">02</div>

                <div>
                  <h2>Target role</h2>
                  <p>What position are you preparing for?</p>
                </div>
              </div>

              <input
                className="setup-input"
                type="text"
                placeholder="e.g. Python Developer"
                value={role}
                onChange={(event) => setRole(event.target.value)}
              />

            </section>


            {/* Experience */}
            <section className="setup-section">

              <div className="setup-section-heading">
                <div className="section-icon">03</div>

                <div>
                  <h2>Experience level</h2>
                  <p>Choose the level that best matches you.</p>
                </div>
              </div>

              <div className="experience-options">

                {["Beginner", "Intermediate", "Advanced"].map((level) => (
                  <button
                    key={level}
                    className={
                      experienceLevel === level ? "experience-option active" : "experience-option"
                    }
                    onClick={() => setExperienceLevel(level)}
                  >
                    <span className="experience-radio"></span>
                    {level}
                  </button>
                ))}

              </div>

            </section>


            {/* Skills */}
            <section className="setup-section">

              <div className="setup-section-heading">
                <div className="section-icon">04</div>

                <div>
                  <h2>Skills</h2>
                  <p>Optional — add skills you want to practice.</p>
                </div>
              </div>

              <input
                className="setup-input"
                type="text"
                placeholder="Python, SQL, FastAPI, Machine Learning..."
                value={skills}
                onChange={(event) => setSkills(event.target.value)}
              />

              <span className="input-hint">
                Separate multiple skills with commas.
              </span>

            </section>

          </div>


          {/* Right summary */}
          <aside className="setup-summary">

            <div className="summary-label">
              YOUR INTERVIEW
            </div>

            <div className="setup-brand">
  <CoachLogo size="sm" />
</div>

            <h2>
              Personalized
              <br />
              practice.
            </h2>

            <p>
              Coach AI will combine your resume, target role,
              and performance to create your interview.
            </p>


            <div className="summary-divider"></div>


            <div className="summary-item">
              <span>Resume</span>
              <strong>
                {resume ? "Uploaded" : "Not uploaded"}
              </strong>
            </div>

            <div className="summary-item">
              <span>Target role</span>
              <strong>
                {role || "Not selected"}
              </strong>
            </div>

            <div className="summary-item">
              <span>Experience</span>
              <strong>{experienceLevel}</strong>
            </div>

            <div className="summary-item">
              <span>Interview</span>
              <strong>5 Questions</strong>
            </div>


            <button
              className="start-setup-btn"
              onClick={handleStartInterview}
              disabled={!resume || !role.trim()}
            >
              <span>Start Interview</span>
              <strong>→</strong>
            </button>

            <small>
              Your resume is used only to personalize this interview.
            </small>

          </aside>

        </div>

      </main>

    </div>
  );
}

export default Setup;