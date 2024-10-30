from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline
import uvicorn

sentiment_pipeline = pipeline("text-classification", model="lxyuan/distilbert-base-multilingual-cased-sentiments-student")

app = FastAPI(
    title="Sentiment Analysis API",
    version="1.0",
    description="A simple API for analyzing sentiment of text."
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str

@app.post("/analyze-sentiment", response_model=SentimentResponse)
async def analyze_sentiment(request: TextRequest):
    try:
        predictions = sentiment_pipeline(request.text)
        sentiment = predictions[0]['label']
        return SentimentResponse(sentiment=sentiment)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)