from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.interview.routes import router as interview_router


app = FastAPI(
    title="Real-Time AI Interviewer"
)


# Allow the React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(interview_router)


@app.get("/")
def home():
    return {
        "message": "Real-Time AI Interviewer API is running!"
    }