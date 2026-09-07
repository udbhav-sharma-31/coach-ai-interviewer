from fastapi import FastAPI

app = FastAPI(title="Real-Time AI Interviewer")


@app.get("/")
def home():
    return {
        "message": "Real-Time AI Interviewer API is running!"
    }