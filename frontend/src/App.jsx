import { BrowserRouter, Routes, Route, useNavigate } from "react-router-dom";
import { AuthProvider } from "./AuthContext";
import "./App.css";
import Auth from "./Auth";
import Home from "./Home";
import Setup from "./Setup";
import Interview from "./Interview";
import Processing from "./Processing";
import Report from "./Report";
import ProtectedRoute from "./ProtectedRoute";
import CoachLogo from "./components/CoachLogo";
function Landing() {
  const navigate = useNavigate();
  return (
    <div className="app">
      <nav className="navbar">
        <div className="navbar-logo">

  <CoachLogo size="sm" />

</div>

        <div className="nav-links">
          <a href="#how-it-works">How It Works</a>
          <a href="#features">Features</a>
          <a href="#technology">Technology</a>
        </div>

        <div className="nav-actions">
          <button
            className="signin-btn"
            onClick={() => navigate("/auth")}
          >
            Sign In
          </button>
          <button
            className="start-btn"
            onClick={() => navigate("/auth")}
          >
            Start Interview
            <span>↗</span>
          </button>
        </div>
      </nav>

      <main className="hero">
        <div className="hero-content">
          <div className="eyebrow">
            <span className="status-dot"></span>
            AI-POWERED INTERVIEW COACH
          </div>

          <h1>
            Your Personal
            <br />
            <span>AI Interview Coach.</span>
          </h1>

          <p className="hero-description">
            Practice smarter with an AI interviewer that understands your
            resume, adapts to your performance, and helps you become
            interview-ready.
          </p>

          <div className="hero-buttons">
            <button
              className="primary-btn"
              onClick={() => navigate("/auth")}
            >
              Start Your Interview
              <span>→</span>
            </button>

            <button className="secondary-btn">
              See How It Works
              <span>↓</span>
            </button>
          </div>

          <div className="hero-stats">
            <div>
              <strong>AI</strong>
              <span>Powered</span>
            </div>

            <div>
              <strong>RAG</strong>
              <span>Resume Aware</span>
            </div>

            <div>
              <strong>24/7</strong>
              <span>Practice</span>
            </div>
          </div>
        </div>

        <div className="hero-visual">
          <div className="glow glow-one"></div>
          <div className="glow glow-two"></div>

          <div className="ai-orb">
            <div className="orb-ring ring-one"></div>
            <div className="orb-ring ring-two"></div>
            <div className="orb-core">
              <span>✦</span>
            </div>
          </div>

          <div className="floating-card card-top">
            <span className="card-icon">◈</span>
            <div>
              <strong>Resume Aware</strong>
              <small>Personalized questions</small>
            </div>
          </div>

          <div className="floating-card card-bottom">
            <span className="card-icon">◉</span>
            <div>
              <strong>Adaptive AI</strong>
              <small>Difficulty adjusts live</small>
            </div>
          </div>
        </div>
      </main>
      <section className="how-it-works" id="how-it-works">
  <div className="section-heading">
    <span>HOW IT WORKS</span>
    <h2>From resume to interview-ready.</h2>
  </div>

  <div className="steps-grid">
    <div className="step-card">
      <span>01</span>
      <h3>Upload Your Resume</h3>
      <p>
        Coach AI reads your resume and builds a personalized understanding
        of your experience and skills.
      </p>
    </div>

    <div className="step-card">
      <span>02</span>
      <h3>Start Your Interview</h3>
      <p>
        Answer realistic questions generated around your background and
        target role.
      </p>
    </div>

    <div className="step-card">
      <span>03</span>
      <h3>Get Evaluated</h3>
      <p>
        Your answers are evaluated and the interview difficulty adapts to
        your performance.
      </p>
    </div>
  </div>
</section>
      <section className="features" id="features">
        <div className="section-heading">
          <span>WHY COACH AI</span>
          <h2>Interview practice that feels real.</h2>
        </div>

        <div className="feature-grid">
          <div className="feature-card">
            <div className="feature-number">01</div>
            <h3>Resume-Aware</h3>
            <p>
              Coach AI reads your resume and asks questions based on your
              actual experience.
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-number">02</div>
            <h3>Adaptive</h3>
            <p>
              Questions become easier or harder based on how you perform.
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-number">03</div>
            <h3>Voice Enabled</h3>
            <p>
              Speak naturally with your AI interviewer or type your answers.
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-number">04</div>
            <h3>Detailed Feedback</h3>
            <p>
              Understand your strengths, weaknesses, and areas to improve.
            </p>
          </div>
        </div>
            </section>

      {/* Technology */}
      <section className="technology" id="technology">
        <div className="section-heading">
          <span>TECHNOLOGY</span>
          <h2>Built with modern AI technology.</h2>
          <p>
            Coach AI combines generative AI, retrieval, custom machine
            learning, and real-time voice technologies to create a
            personalized interview experience.
          </p>
        </div>

        <div className="technology-grid">

          <div className="technology-card">
            <div className="technology-number">01</div>
            <h3>Generative AI</h3>
            <p>
              Local Qwen models generate personalized interview questions,
              evaluate general answers, and create the final interview report.
            </p>
            <div className="technology-tags">
              <span>Qwen 3</span>
              <span>LLM</span>
            </div>
          </div>

          <div className="technology-card">
            <div className="technology-number">02</div>
            <h3>Custom Transformer</h3>
            <p>
              A custom-trained Transformer evaluates technical interview
              answers using a specialized answer-quality classification model.
            </p>
            <div className="technology-tags">
              <span>PyTorch</span>
              <span>Transformer</span>
            </div>
          </div>

          <div className="technology-card">
            <div className="technology-number">03</div>
            <h3>RAG & Resume Intelligence</h3>
            <p>
              Resume content is extracted, chunked, embedded, and retrieved
              to ground interview questions in the candidate's actual profile.
            </p>
            <div className="technology-tags">
              <span>FAISS</span>
              <span>Embeddings</span>
              <span>PyPDF</span>
            </div>
          </div>

          <div className="technology-card">
            <div className="technology-number">04</div>
            <h3>AI Orchestration</h3>
            <p>
              LangGraph coordinates the interview workflow, including
              questioning, evaluation, adaptive difficulty, and reporting.
            </p>
            <div className="technology-tags">
              <span>LangGraph</span>
              <span>FastAPI</span>
            </div>
          </div>

          <div className="technology-card">
            <div className="technology-number">05</div>
            <h3>Voice Interview</h3>
            <p>
              Candidates can interact naturally using speech while questions
              are spoken aloud and answers can be transcribed in real time.
            </p>
            <div className="technology-tags">
              <span>STT</span>
              <span>TTS</span>
              <span>Web Speech API</span>
            </div>
          </div>

          <div className="technology-card">
            <div className="technology-number">06</div>
            <h3>Secure Authentication</h3>
            <p>
              User accounts are protected with Supabase authentication,
              supporting email/password login and Google Sign-In.
            </p>
            <div className="technology-tags">
              <span>Supabase</span>
              <span>OAuth</span>
            </div>
          </div>

        </div>
      </section>
    </div>
  );
}
function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/auth" element={<Auth />} />
       <Route
  path="/home"
  element={
    <ProtectedRoute>
      <Home />
    </ProtectedRoute>
  }
/>

<Route
  path="/setup"
  element={
    <ProtectedRoute>
      <Setup />
    </ProtectedRoute>
  }
/>

<Route
  path="/interview"
  element={
    <ProtectedRoute>
      <Interview />
    </ProtectedRoute>
  }
/>

<Route
  path="/processing"
  element={
    <ProtectedRoute>
      <Processing />
    </ProtectedRoute>
  }
/>

<Route
  path="/report"
  element={
    <ProtectedRoute>
      <Report />
    </ProtectedRoute>
  }
/>
      </Routes>
      </AuthProvider>
    </BrowserRouter>
  );
}
export default App;