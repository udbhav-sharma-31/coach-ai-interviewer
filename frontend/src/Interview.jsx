import { useEffect, useRef, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import "./Interview.css";
import CoachLogo from "./components/CoachLogo";

function Interview() {
  const navigate = useNavigate();
  const location = useLocation();

const {
  sessionId,
  question: initialQuestion,
  questionNumber: initialQuestionNumber,
  difficulty: initialDifficulty,
  role,
} = location.state || {};

  const [question, setQuestion] = useState(
    initialQuestion ||
      "Can you describe a challenging project you worked on and how you approached solving it?"
  );

  const [questionNumber, setQuestionNumber] = useState(
    initialQuestionNumber || 1
  );

  const [difficulty, setDifficulty] = useState(
    initialDifficulty || "beginner"
  );

  const [answer, setAnswer] = useState("");

  const [messages, setMessages] = useState([
    {
      type: "ai",
      text:
        initialQuestion ||
        "Can you describe a challenging project you worked on and how you approached solving it?",
    },
  ]);
  const conversationEndRef = useRef(null);
  const [isSpeaking, setIsSpeaking] = useState(true);
  const [isListening, setIsListening] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const recognitionRef = useRef(null);
  useEffect(() => {
  if (!question) {
    return;
  }

  const timer = setTimeout(() => {
    speakQuestion(question);
  }, 300);

  return () => {
    clearTimeout(timer);
    window.speechSynthesis.cancel();
  };
}, [question]);
useEffect(() => {
  if (!conversationEndRef.current) {
    return;
  }

  conversationEndRef.current.scrollIntoView({
    behavior: "smooth",
    block: "end",
  });
}, [question, answer]);
useEffect(() => {
  return () => {
    if (recognitionRef.current) {
      recognitionRef.current.stop();
    }

    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
    }
  };
}, []);
  const speakQuestion = (text) => {
  if (!text || !("speechSynthesis" in window)) {
    return;
  }

  window.speechSynthesis.cancel();

  const utterance = new SpeechSynthesisUtterance(text);

  utterance.rate = 0.95;
  utterance.pitch = 1;
  utterance.volume = 1;

  utterance.onstart = () => {
    setIsSpeaking(true);
  };

  utterance.onend = () => {
    setIsSpeaking(false);
  };

  utterance.onerror = () => {
    setIsSpeaking(false);
  };

  window.speechSynthesis.speak(utterance);
};

const toggleSpeaking = () => {
  if (isSpeaking) {
    window.speechSynthesis.cancel();
    setIsSpeaking(false);
    return;
  }

  speakQuestion(question);
};

  const toggleListening = () => {
  if (isSubmitting) {
    return;
  }

  // Stop Coach AI from speaking when the candidate
  // starts recording an answer.
  if ("speechSynthesis" in window) {
    window.speechSynthesis.cancel();
  }

  setIsSpeaking(false);

  const SpeechRecognition =
    window.SpeechRecognition ||
    window.webkitSpeechRecognition;

  if (!SpeechRecognition) {
    alert(
      "Speech recognition is not supported in this browser. Please use Chrome or another supported browser."
    );
    return;
  }

  // Stop listening
  if (isListening) {
    if (recognitionRef.current) {
      recognitionRef.current.stop();
    }

    setIsListening(false);
    return;
  }

  // Create a new recognition instance
  const recognition = new SpeechRecognition();

  recognition.continuous = true;

  // IMPORTANT:
  // Only process final speech results.
  // This prevents interim speech from being
  // repeatedly appended to the answer.
  recognition.interimResults = false;

  recognition.lang = "en-US";

  recognition.onstart = () => {
    setIsListening(true);
  };

  recognition.onresult = (event) => {
    let finalTranscript = "";

    for (
      let i = event.resultIndex;
      i < event.results.length;
      i++
    ) {
      if (event.results[i].isFinal) {
        finalTranscript +=
          event.results[i][0].transcript;
      }
    }

    finalTranscript = finalTranscript.trim();

    if (!finalTranscript) {
      return;
    }

    setAnswer((previousAnswer) => {
      const separator =
        previousAnswer.trim().length > 0
          ? " "
          : "";

      return (
        previousAnswer.trim() +
        separator +
        finalTranscript
      ).slice(0, 2000);
    });
  };

  recognition.onerror = (event) => {
    console.error(
      "Speech recognition error:",
      event.error
    );

    setIsListening(false);
  };

  recognition.onend = () => {
    setIsListening(false);
  };

  recognitionRef.current = recognition;

  recognition.start();
};

  const handleSubmit = async () => {
    if (!answer.trim() || !sessionId || isSubmitting) {
      return;
    }

    const submittedAnswer = answer.trim();

    setIsSubmitting(true);

    // Show candidate's answer immediately in the conversation.
    setMessages((previousMessages) => [
      ...previousMessages,
      {
        type: "candidate",
        text: submittedAnswer,
      },
    ]);

    // Clear the input so it cannot be submitted again accidentally.
    setAnswer("");

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/interview/answer",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            session_id: sessionId,
            answer: submittedAnswer,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        console.error("Answer submission failed:", data);
        return;
      }

      console.log("Answer evaluated:", data);

      // Interview finished.
      if (data.finished) {
  navigate("/processing", {
  state: {
    sessionId: sessionId,
    report: {
  sessionId: sessionId,
  role: role,
  questions: data.questions,
  answers: data.answers,
  evaluations: data.evaluations,
  overallScore: data.overall_score,
  difficulty: data.difficulty,
  finalReport: data.final_report,
},
  },
});

  return;
}

      // Backend generated the next question.
      const nextQuestion =
        data.next_question ||
        data.question ||
        data.current_question;

      if (nextQuestion) {
        setQuestion(nextQuestion);

        setQuestionNumber(
          data.question_number || questionNumber + 1
        );

        setDifficulty(
          data.difficulty || difficulty
        );

        // Add the next AI question to the conversation.
        setMessages((previousMessages) => [
          ...previousMessages,
          {
            type: "ai",
            text: nextQuestion,
          },
        ]);

        // Make the AI appear to speak the new question.
        setIsSpeaking(true);
      }

    } catch (error) {
      console.error(
        "Could not submit answer:",
        error
      );
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="interview-page">

      <div className="interview-glow interview-glow-one"></div>
      <div className="interview-glow interview-glow-two"></div>

      <header className="interview-header">

        <button
          className="interview-logo"
          onClick={() => navigate("/home")}
        >
          <div className="interview-brand">
  <CoachLogo size="sm" />
</div>
          <div className="logo-text">COACH AI</div>
        </button>

        <div className="interview-progress">

          <span>
            {String(questionNumber).padStart(2, "0")}
          </span>

          <div className="progress-track">
            <div
              className="progress-fill"
              style={{
                width: `${(questionNumber / 5) * 100}%`,
              }}
            ></div>
          </div>

          <span>05</span>

        </div>

        <div className="difficulty-badge">

          <span></span>

          {difficulty.charAt(0).toUpperCase() +
            difficulty.slice(1)}

        </div>

      </header>

      <main className="interview-room">

        <section className="ai-area">

          <button
            className={`ai-orb ${
              isSpeaking ? "speaking" : ""
            }`}
            onClick={toggleSpeaking}
            aria-label="Toggle AI speaking"
          >

            <div className="orb-ring ring-one"></div>
            <div className="orb-ring ring-two"></div>
            <div className="orb-ring ring-three"></div>

            <div className="orb-core">
              <span>✦</span>
            </div>

          </button>

          <div className="ai-status">

            <span className="status-dot"></span>

            {isSubmitting
              ? "ANALYZING RESPONSE"
              : isSpeaking
              ? "AI IS SPEAKING"
              : "AI INTERVIEWER"}

          </div>

        </section>

        <section className="conversation">

  <div className="conversation-label">
    CONVERSATION
  </div>

  <div className="conversation-history">

    {messages.map((message, index) => (

      <div
        key={index}
        className={`message-row ${
          message.type === "ai"
            ? "ai-message"
            : "candidate-message"
        }`}
      >

        <div className="message-meta">

          <span className="message-dot"></span>

          {message.type === "ai"
            ? "COACH AI"
            : "YOU"}

        </div>

        <div className="message-bubble">

          <p>{message.text}</p>

          {message.type === "ai" &&
            index === messages.length - 1 && (

              <button
                className="listen-btn"
                onClick={toggleSpeaking}
                disabled={isSubmitting}
              >
                <span>🔊</span>

                {isSpeaking
                  ? "Speaking..."
                  : "Listen again"}

              </button>

            )}

        </div>
      <div ref={conversationEndRef} />
      </div>

    ))}

    {isSubmitting && (

      <div className="message-row ai-message">

        <div className="message-meta">

          <span className="message-dot"></span>

          COACH AI

        </div>

        <div className="message-bubble analyzing-bubble">

          <p>
            Analyzing your response...
          </p>

        </div>

      </div>

    )}

  </div>

</section>

        <section className="response-area">

          <div className="response-heading">

            <div>

              <span>YOUR RESPONSE</span>

              <p>
                Speak naturally or type your answer.
              </p>

            </div>

            <span className="character-count">
              {answer.length} / 2000
            </span>

          </div>

          <div className="response-box">

            <textarea
              value={answer}
              maxLength={2000}
              disabled={isSubmitting}
              onChange={(event) =>
                setAnswer(event.target.value)
              }
              placeholder={
                isSubmitting
                  ? "Analyzing your answer..."
                  : isListening
                  ? "Listening to your answer..."
                  : "Type your answer..."
              }
            />

            <div className="response-controls">

              <button
                className={`voice-btn ${
                  isListening ? "listening" : ""
                }`}
                onClick={toggleListening}
                disabled={isSubmitting}
              >

                <span>
                  {isListening ? "●" : "🎤"}
                </span>

                {isListening
                  ? "Listening..."
                  : "Speak Answer"}

              </button>

              <button
                className="submit-answer-btn"
                onClick={handleSubmit}
                disabled={
                  !answer.trim() ||
                  !sessionId ||
                  isSubmitting
                }
              >

                {isSubmitting
                  ? "Analyzing..."
                  : "Submit"}

                <span>
                  {isSubmitting ? "..." : "→"}
                </span>

              </button>

            </div>

          </div>

        </section>

        <div className="room-footer">

          <span>
            QUESTION{" "}
            <strong>
              {String(questionNumber).padStart(2, "0")}
            </strong>{" "}
            OF <strong>05</strong>
          </span>

          <span>•</span>

          <span>ADAPTIVE INTERVIEW</span>

          <span>•</span>

          <span>RESUME AWARE</span>

        </div>

      </main>

    </div>
  );
}

export default Interview;