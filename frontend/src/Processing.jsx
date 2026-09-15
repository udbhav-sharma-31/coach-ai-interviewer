import { useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import "./Processing.css";

function Processing() {
  const navigate = useNavigate();
  const location = useLocation();

  const report = location.state?.report;

  useEffect(() => {
  const timer = setTimeout(() => {
    navigate("/report", {
      state: {
        report: report,
      },
    });
  }, 4000);

  return () => clearTimeout(timer);
}, [navigate, report]);

  return (
    <div className="processing-page">

      <div className="processing-glow"></div>

      <div className="processing-content">

        <div className="processing-orb">

          <div className="processing-ring ring-a"></div>
          <div className="processing-ring ring-b"></div>
          <div className="processing-ring ring-c"></div>

          <div className="processing-core">
            ✦
          </div>

        </div>

        <div className="processing-label">
          COACH AI
        </div>

        <h1>
          Analyzing your
          <span> interview.</span>
        </h1>

        <p>
          Reviewing your answers, performance,
          and interview progress.
        </p>

        <div className="processing-dots">
          <span></span>
          <span></span>
          <span></span>
        </div>

        <div className="processing-status">
          Preparing your personalized feedback
        </div>

      </div>

    </div>
  );
}

export default Processing;