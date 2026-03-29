from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import logging

# This imports your AI brain from the agents folder
from agents.orchestrator import MultiAgentOrchestrator

app = FastAPI(title="MyET AI Platform")

# Configure CORS so your React frontend (localhost:3000) can talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# User preferences to guide the AI's personalization
USER_PREFS = {
    "interests": ["Technology", "AI", "Finance"],
    "reading_level": "Professional",
    "role": "Software Engineer"
}

class NewsRequest(BaseModel):
    topic: str

# --- GLOBAL EXCEPTION HANDLER ---
# This is the "Debugger". If you get a 500 error, it will PRINT the 
# real reason in your terminal so we can fix it!
@app.exception_handler(Exception)
async def debug_exception_handler(request: Request, exc: Exception):
    print(f"\n❌ CRITICAL ERROR DETECTED: {str(exc)}\n")
    return JSONResponse(
        status_code=500,
        content={"status": "error", "message": str(exc)},
    )

@app.get("/")
async def health_check():
    return {"status": "online", "message": "MyET Backend is running"}

@app.post("/api/generate-feed")
async def generate_personalized_feed(request: NewsRequest):
    # This triggers the Multi-Agent Pipeline
    orchestrator = MultiAgentOrchestrator(user_preferences=USER_PREFS)
    
    # Run the pipeline (Aggregation -> Summarization -> Insights)
    results = await orchestrator.process_news_pipeline(request.topic)
    
    return {"status": "success", "data": results}

if __name__ == "__main__":
    import uvicorn
    # Start the server on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)