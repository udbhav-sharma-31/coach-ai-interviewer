import "./CoachLogo.css";

function CoachLogo({
  size = "md",
  iconOnly = false,
}) {
  return (
    <div
      className={`coach-logo coach-logo-${size} ${
        iconOnly ? "coach-logo-icon-only" : ""
      }`}
    >
      <svg
  className="coach-logo-mark"
  viewBox="0 0 100 100"
  fill="none"
  xmlns="http://www.w3.org/2000/svg"
  aria-label="Coach AI logo"
>
  <defs>
    <linearGradient
      id="coachLogoGradient"
      x1="15"
      y1="20"
      x2="85"
      y2="80"
      gradientUnits="userSpaceOnUse"
    >
      <stop offset="0%" stopColor="#06D9FF" />
      <stop offset="28%" stopColor="#168BFF" />
      <stop offset="55%" stopColor="#684CFF" />
      <stop offset="78%" stopColor="#B936FF" />
      <stop offset="100%" stopColor="#FF38D1" />
    </linearGradient>

    <filter
      id="coachLogoGlow"
      x="-50%"
      y="-50%"
      width="200%"
      height="200%"
    >
      <feGaussianBlur
        stdDeviation="3.5"
        result="blur"
      />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  {/* Soft outer glow */}
  <path
    d="
      M76 18
      C64 10 49 8 36 13
      C21 18 11 31 10 46
      C8 62 16 77 29 86
      C42 95 59 96 73 88
      C87 80 94 66 92 51
      C91 37 85 26 76 18
    "
    stroke="url(#coachLogoGradient)"
    strokeWidth="11"
    strokeLinecap="round"
    opacity="0.22"
    filter="url(#coachLogoGlow)"
  />

  {/* Main fluid ring */}
  <path
    d="
      M76 18
      C64 10 49 8 36 13
      C21 18 11 31 10 46
      C8 62 16 77 29 86
      C42 95 59 96 73 88
      C87 80 94 66 92 51
      C91 37 85 26 76 18
    "
    stroke="url(#coachLogoGradient)"
    strokeWidth="7"
    strokeLinecap="round"
    filter="url(#coachLogoGlow)"
  />

  {/* Fluid wave accents */}
  <path
    d="
      M17 65
      C23 69 25 76 31 78
      C37 80 40 87 45 90
    "
    stroke="url(#coachLogoGradient)"
    strokeWidth="5"
    strokeLinecap="round"
    opacity="0.9"
  />

  <path
    d="
      M57 11
      C62 16 68 16 73 20
      C79 24 84 29 86 35
    "
    stroke="url(#coachLogoGradient)"
    strokeWidth="5"
    strokeLinecap="round"
    opacity="0.85"
  />

  <path
    d="
      M84 63
      C82 69 77 72 73 77
      C69 82 64 86 58 89
    "
    stroke="url(#coachLogoGradient)"
    strokeWidth="5"
    strokeLinecap="round"
    opacity="0.8"
  />
</svg>

      {!iconOnly && (
        <div className="coach-logo-wordmark">
          <span>COACH</span>
          <strong>AI</strong>
        </div>
      )}
    </div>
  );
}

export default CoachLogo;