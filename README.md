# MyET-Hackathon-Project
MyET is an AI-native platform that transforms tech news into personalized intelligence. Built with FastAPI and React, it uses a Multi-Agent Orchestration system with Gemini 2.5 to provide role-specific career insights through specialized parallel processing agents. Optimized for speed and relevance.

# MyET: AI-Native News Experience 

**MyET** is an intelligent news analysis platform built for the **ET Gen AI Hackathon 2026**. It transforms static business and tech news into deeply personalized, actionable intelligence using a **Multi-Agent Orchestration** system powered by the **Google Gemini 2.5** series.

## The Innovation: "Personalized Relevance"
Traditional news aggregators provide the same content to everyone. **MyET** solves this by using AI Agents to answer the critical question: *"Why does this matter to ME?"* based on the user's specific professional role and interests (Software Engineering, AI, and Finance).

## Architecture: Multi-Agent Orchestration
The system uses a high-performance parallel pipeline to process news at scale:
- **Summarization Agent:** Distills complex articles into high-impact, single-sentence summaries using Gemini 2.5 Flash.
- **Insight Agent:** Maps article themes to the user's specific career goals and technical background.
- **Orchestrator:** Coordinates these agents using `asyncio.gather` for maximum speed, reducing response latency by 50%.

## Tech Stack
- **Frontend:** React (Vite) + Tailwind CSS (Modern, Responsive UI)
- **Backend:** FastAPI (Python 3.10+) + Uvicorn
- **AI Engine:** Google Gemini SDK (`google-genai`)
- **Concurrency:** Python `asyncio` for parallel agent execution.

**PROJECT ARCHITECTURE** :
```
MyET-Hackathon-Project/
├── backend/                     # Python / FastAPI Backend
│   ├── agents/                  # AI Agent Module
│   │   ├── __init__.py
│   │   └── orchestrator.py      # Multi-agent logic
│   ├── main.py                  # API Routing
│   └── requirements.txt         # Python dependencies
│
└── frontend/                    # React Frontend
    ├── public/
    │   └── index.html
    ├── src/
    │   ├── components/
    │   │   └── InsightCard.jsx  # UI for news and insights
    │   ├── App.jsx              # Main interface and API calls
    │   ├── index.js             # React entry point
    │   └── index.css            # Global styles
    ├── package.json
    └── tailwind.config.js       # Styling configuration
        
```
    
## Quick Start (Local Setup)

** 1. Backend Setup**

''' Open bash

cd backend

pip install fastapi uvicorn pydantic google-genai

Ensure your Gemini API Key is set in agents/orchestrator.py

python main.py

** 2. Frontend Setup**

cd frontend

npm install

npm start

The app will be available at http://localhost:3000

**Key Features** :

Role-Based Analysis: Tailors insights for Software Engineers, providing technical context like security protocols and system impacts.

Async Execution: Utilizes asynchronous programming to handle multiple AI requests simultaneously.

Developer-Ready API: Full Swagger documentation available at localhost:8000/docs.

**Contributors** :
Korivi Varshitha - Project Collaborator

Developed for the ET_AI_Hackathon 2026.
