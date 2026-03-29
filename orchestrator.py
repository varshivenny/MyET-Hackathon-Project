import asyncio
from google import genai
from pydantic import BaseModel
from typing import List, Dict

# Initialize the new Client
# TIP: You can also set this as an environment variable 'GEMINI_API_KEY'
client = genai.Client(api_key="AIzaSyDX5Dp1RsSCC4Ro_twoS5qRWW8XimtPlX0")

class ProcessedArticle(BaseModel):
    headline: str
    summary: str
    contextual_insight: str
    relevance_score: float

class MockArticle(BaseModel):
    title: str
    content: str
    relevance_score: float

class SummarizationAgent:
    async def generate_concise_summary(self, content: str) -> str:
        # Use the NEW asynchronous 'aio' client
        response = await client.aio.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Summarize this news in one short sentence: {content}"
        )
        return response.text.strip()

class InsightAgent:
    async def generate_impact_analysis(self, content: str, prefs: Dict) -> str:
        interests = ", ".join(prefs.get('interests', []))
        role = prefs.get('role', 'Student')
        
        prompt = f"As a {role} interested in {interests}, why does this news matter? {content}"
        # Use the NEW asynchronous 'aio' client
        response = await client.aio.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text.strip()

class MultiAgentOrchestrator:
    def __init__(self, user_preferences: Dict):
        self.user_preferences = user_preferences
        self.summarizer = SummarizationAgent()
        self.insight_engine = InsightAgent()

    async def process_news_pipeline(self, topic_query: str) -> List[ProcessedArticle]:
        # 1. Content Aggregation (Simulated for Hackathon)
        raw_articles = [
            MockArticle(
                title=f"New Breakthrough in {topic_query}", 
                content=f"Researchers announced a major shift in {topic_query} today, impacting global markets.", 
                relevance_score=0.98
            ),
            MockArticle(
                title=f"{topic_query} Regulations 2026", 
                content=f"The government has released new safety guidelines for {topic_query} implementation.", 
                relevance_score=0.85
            )
        ]
        
        results = []
        for article in raw_articles:
            # We run the agents concurrently using asyncio.gather for max speed!
            summary_task = self.summarizer.generate_concise_summary(article.content)
            insight_task = self.insight_engine.generate_impact_analysis(article.content, self.user_preferences)
            
            summary, insight = await asyncio.gather(summary_task, insight_task)
            
            results.append(ProcessedArticle(
                headline=article.title,
                summary=summary,
                contextual_insight=insight,
                relevance_score=article.relevance_score
            ))
        return results