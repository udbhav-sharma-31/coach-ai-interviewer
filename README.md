# Coach AI — Real-Time AI Interviewer

> Your Personal AI Interview Coach

Coach AI is a real-time AI-powered interview platform that conducts personalized interviews based on a candidate's resume and target role.

It combines **RAG, LangGraph, local LLMs, a custom Transformer model, FastAPI, React, and browser-based speech technologies** to create an adaptive interview experience.

## ✨ Features

- 📄 Resume-based personalized interviews
- 🔎 RAG-powered resume retrieval using embeddings and FAISS
- 🤖 AI-powered interview question generation
- 🧠 Custom Transformer for technical answer evaluation
- 🔀 Hybrid Transformer + Qwen evaluation
- 💬 General/open-ended answer evaluation using Qwen
- 📈 Adaptive interview difficulty
- 🕸️ LangGraph-based interview orchestration
- 🎙️ Voice questions using Text-to-Speech
- 🎤 Spoken answers using Speech-to-Text
- ⌨️ Text-answer support
- 📊 AI-generated final performance report
- 🔐 Supabase authentication
- 📚 Interview history for authenticated users

---

## 🏗️ Architecture

```text
Candidate
    │
    ▼
React Frontend
    │
    ▼
FastAPI Backend
    │
    ▼
LangGraph Interview Brain
    │
    ├───────────────┬────────────────┐
    ▼               ▼                ▼
Resume Pipeline  Question Engine  Evaluation Engine
    │               │                │
    ▼               ▼                ▼
PDF Extraction   Local Qwen      Evaluation Router
    │                                │
    ▼                         ┌──────┴──────┐
Chunking                      ▼             ▼
    │                     Technical      General
    ▼                     Evaluation     Evaluation
Embeddings                    │             │
    │                         ▼             ▼
    ▼                   Custom Transformer Qwen
FAISS
    │
    └──────────────────────┬───────────────┘
                           ▼
                    Final Evaluation
                           │
                           ▼
                    Difficulty Engine
                           │
                           ▼
                     Next Question
                           │
                           ▼
                      Final Report