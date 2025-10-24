from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI(
    title="Cognitive Sentiment Analysis Microservice",
    description="A microservice that analyzes the sentiment of input text.",
    version="1.0.0"
)

# Define request body
class TextInput(BaseModel):
    text: str

# Load pre-trained sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

@app.post("/analyze")
async def analyze_sentiment(input: TextInput):
    """Analyze sentiment of a given text."""
    result = sentiment_pipeline(input.text)[0]
    return {
        "label": result["label"],  # e.g., "POSITIVE" or "NEGATIVE"
        "score": round(result["score"], 3)
    }

@app.get("/")
def root():
    return {"message": "Cognitive Sentiment Analysis Microservice is running."}
