import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { supabase } from "./lib/supabase";
import { useAuth } from "./AuthContext";
import CoachLogo from "./components/CoachLogo";
import "./Auth.css";

function Auth() {
  const navigate = useNavigate();
  const { user, loading: authLoading } = useAuth();
  const [isLogin, setIsLogin] = useState(true);

  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  useEffect(() => {
  if (!authLoading && user) {
    navigate("/home", { replace: true });
  }
}, [user, authLoading, navigate]);
  const handleAuth = async (event) => {
    event.preventDefault();

    setError("");
    setSuccess("");

    if (!email.trim() || !password.trim()) {
      setError("Please enter your email and password.");
      return;
    }

    if (!isLogin && !fullName.trim()) {
      setError("Please enter your full name.");
      return;
    }

    setLoading(true);

    try {
      if (isLogin) {
        const { error: loginError } =
          await supabase.auth.signInWithPassword({
            email: email.trim(),
            password,
          });

        if (loginError) {
          throw loginError;
        }

        navigate("/home");
      } else {
        const { data, error: signupError } =
          await supabase.auth.signUp({
            email: email.trim(),
            password,
            options: {
              data: {
                full_name: fullName.trim(),
              },
            },
          });

        if (signupError) {
          throw signupError;
        }

        if (data.session) {
          navigate("/home");
        } else {
          setSuccess(
            "Account created successfully. Please check your email to confirm your account."
          );
        }
      }
    } catch (authError) {
      console.error("Authentication error:", authError);

      setError(
        authError.message ||
          "Something went wrong. Please try again."
      );
    } finally {
      setLoading(false);
    }
  };

  const handleGoogleLogin = async () => {
    setError("");
    setSuccess("");
    setLoading(true);

    try {
      const { error: googleError } =
        await supabase.auth.signInWithOAuth({
          provider: "google",
          options: {
            redirectTo: `${window.location.origin}/auth`,
          },
        });

      if (googleError) {
        throw googleError;
      }
    } catch (authError) {
      console.error("Google authentication error:", authError);

      setError(
        authError.message ||
          "Unable to continue with Google."
      );

      setLoading(false);
    }
  };

  const switchMode = (loginMode) => {
    setIsLogin(loginMode);
    setError("");
    setSuccess("");
    setPassword("");
  };

  return (
    <div className="auth-page">
      <div className="auth-glow auth-glow-one"></div>
      <div className="auth-glow auth-glow-two"></div>

      <div className="auth-brand">
  <CoachLogo size="sm" />
</div>

      <main className="auth-container">
        <div className="auth-card">

          <div className="auth-header">
            <div className="auth-icon">
  <CoachLogo size="md" iconOnly />
</div>

            <h1>
              {isLogin
                ? "Welcome Back"
                : "Create Your Account"}
            </h1>

            <p>
              {isLogin
                ? "Continue your journey to interview confidence."
                : "Start preparing smarter with your personal AI coach."}
            </p>
          </div>

          <div className="auth-toggle">
            <button
              type="button"
              className={isLogin ? "active" : ""}
              onClick={() => switchMode(true)}
            >
              Login
            </button>

            <button
              type="button"
              className={!isLogin ? "active" : ""}
              onClick={() => switchMode(false)}
            >
              Sign Up
            </button>
          </div>

          <form onSubmit={handleAuth}>

            {!isLogin && (
              <div className="input-group">
                <label>Full Name</label>

                <input
                  type="text"
                  placeholder="Enter your name"
                  value={fullName}
                  onChange={(event) =>
                    setFullName(event.target.value)
                  }
                />
              </div>
            )}

            <div className="input-group">
              <label>Email Address</label>

              <input
                type="email"
                placeholder="you@example.com"
                value={email}
                onChange={(event) =>
                  setEmail(event.target.value)
                }
              />
            </div>

            <div className="input-group">
              <label>Password</label>

              <input
                type="password"
                placeholder="Enter your password"
                value={password}
                onChange={(event) =>
                  setPassword(event.target.value)
                }
              />
            </div>

            {isLogin && (
              <div className="forgot-password">
                <button
                  type="button"
                  onClick={() =>
                    setError(
                      "Password reset will be added next."
                    )
                  }
                >
                  Forgot password?
                </button>
              </div>
            )}

            {error && (
              <div className="auth-message auth-error">
                {error}
              </div>
            )}

            {success && (
              <div className="auth-message auth-success">
                {success}
              </div>
            )}

            <button
              type="submit"
              className="auth-submit"
              disabled={loading}
            >
              {loading
                ? "Please wait..."
                : isLogin
                ? "Login to Coach AI"
                : "Create Account"}

              {!loading && <span>→</span>}
            </button>

          </form>

          <div className="auth-divider">
            <span></span>
            <p>OR</p>
            <span></span>
          </div>

          <button
            type="button"
            className="google-btn"
            onClick={handleGoogleLogin}
            disabled={loading}
          >
            <span className="google-icon">G</span>
            Continue with Google
          </button>

          <p className="auth-switch">
            {isLogin
              ? "Don't have an account?"
              : "Already have an account?"}

            <button
              type="button"
              onClick={() => switchMode(!isLogin)}
            >
              {isLogin
                ? " Create one"
                : " Login"}
            </button>
          </p>

        </div>
      </main>

      <div className="auth-footer">
        <span>COACH AI</span>
        <p>Your Personal AI Interview Coach</p>
      </div>
    </div>
  );
}

export default Auth;