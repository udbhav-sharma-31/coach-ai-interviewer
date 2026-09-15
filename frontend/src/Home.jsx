import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Home.css";
import { useAuth } from "./AuthContext";
import CoachLogo from "./components/CoachLogo";
function Home() {
  const navigate = useNavigate();
  const { user, logout } = useAuth();
  const displayName =
  user?.user_metadata?.full_name ||
  user?.email?.split("@")[0] ||
  "User";

const firstName = displayName.split(" ")[0];

const avatarLetter = firstName.charAt(0).toUpperCase();
const [interviewHistory, setInterviewHistory] = useState([]);
const latestInterview = interviewHistory[0];
useEffect(() => {
  if (!user?.id) {
    return;
  }

  const historyKey =
    `coach_ai_interview_history_${user.id}`;

  const history = JSON.parse(
    localStorage.getItem(historyKey) || "[]"
  );

  setInterviewHistory(history);
}, [user]);
  return (
    <div className="home-page">

      {/* Background */}
      <div className="home-glow home-glow-one"></div>
      <div className="home-glow home-glow-two"></div>

      {/* Navbar */}
      <nav className="home-navbar">

        <div className="navbar-logo">
  <CoachLogo size="sm" />
</div>
        <button
  className="home-logout-btn"
  onClick={logout}
>
  Logout
</button>
        <div className="home-nav-links">
          <a href="#dashboard">Dashboard</a>
          <a href="#history">Interview History</a>
        </div>

        <div className="home-nav-right">
          <div className="profile-avatar">
  {avatarLetter}
</div>
        </div>

      </nav>


      {/* Main Content */}
      <main className="home-content">

        {/* Welcome */}
        <section className="welcome-section">

          <div>
            <span className="home-eyebrow">
              ✦ YOUR AI INTERVIEW COACH
            </span>

            <h1>
  Welcome back,
  <br />
  <span>{firstName}.</span>
</h1>

            <p>
              Ready to sharpen your interview skills?
              Start a personalized practice session.
            </p>
          </div>

          <button
            className="new-interview-btn"
            onClick={() => navigate("/setup")}
          >
            <span>Start New Interview</span>
            <strong>↗</strong>
          </button>

        </section>


        {/* Main Dashboard Cards */}
        <section className="dashboard-grid" id="dashboard">

          {/* Start Interview Card */}
          <div className="start-interview-card">

            <div className="card-glow"></div>

            <div className="interview-card-top">
              <div className="navbar-logo">
  <CoachLogo size="sm" />
</div>

              <span>READY TO PRACTICE</span>
            </div>

            <h2>
              Your next interview
              <br />
              starts here.
            </h2>

            <p>
              Upload your resume, choose your target role,
              and let Coach AI create a personalized interview.
            </p>

            <button
              onClick={() => navigate("/setup")}
              className="card-start-btn"
            >
              Begin Interview
              <span>→</span>
            </button>

          </div>


          {/* Performance Card */}
          <div className="performance-card">

            <div className="small-card-header">
              <div>
                <span>YOUR PERFORMANCE</span>
                <h3>Interview Score</h3>
              </div>

              <div className="score-icon">
                ◈
              </div>
            </div>

            <div className="score-display">
  <strong>
    {latestInterview
      ? Number(latestInterview.score).toFixed(1)
      : "--"}
  </strong>
  <span>/ 10</span>
</div>
            <p>
              Complete your first interview to see
              your performance score.
            </p>

          </div>

        </section>


        {/* Features / Status */}
        <section className="status-section">

          <div className="section-title">
            <span>COACH AI CAPABILITIES</span>
            <h2>Built around you.</h2>
          </div>

          <div className="status-grid">

            <div className="status-card">
              <div className="status-icon">◈</div>

              <div>
                <h3>Resume-Aware</h3>
                <p>
                  Questions based on your actual experience.
                </p>
              </div>

              <span className="status-active">
                Ready
              </span>
            </div>


            <div className="status-card">
              <div className="status-icon">◉</div>

              <div>
                <h3>Adaptive Difficulty</h3>
                <p>
                  Questions adapt to your performance.
                </p>
              </div>

              <span className="status-active">
                Active
              </span>
            </div>


            <div className="status-card">
              <div className="status-icon">◎</div>

              <div>
                <h3>Voice Interview</h3>
                <p>
                  Speak naturally or type your answer.
                </p>
              </div>

              <span className="status-active">
                Ready
              </span>
            </div>

          </div>

        </section>


        {/* Interview History */}
<section className="history-section" id="history">

  <div className="section-title history-title">
    <div>
      <span>YOUR ACTIVITY</span>
      <h2>Recent Interviews</h2>
    </div>

    <button className="view-all-btn">
      View All →
    </button>
  </div>

  {interviewHistory.length === 0 ? (

    <div className="empty-history">

      <div className="empty-icon">
        ◌
      </div>

      <h3>No interviews yet</h3>

      <p>
        Your completed interviews and performance
        reports will appear here.
      </p>

      <button
        onClick={() => navigate("/setup")}
      >
        Start Your First Interview
      </button>

    </div>

  ) : (

    <div className="interview-history-list">

      {interviewHistory.slice(0, 5).map((interview) => (

        <div
          className="history-item"
          key={interview.id}
        >

          <div className="history-main">

            <h3>{interview.role}</h3>

            <span>
              {new Date(interview.date).toLocaleDateString(
                "en-IN",
                {
                  day: "numeric",
                  month: "short",
                  year: "numeric",
                }
              )}
            </span>

          </div>

          <div className="history-meta">

            <strong>
              {Number(interview.score).toFixed(1)}
              <small>/10</small>
            </strong>

            <span>{interview.difficulty}</span>

          </div>

        </div>

      ))}

    </div>

  )}

</section>

      </main>

    </div>
  );
}

export default Home;