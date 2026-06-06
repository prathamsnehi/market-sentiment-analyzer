from pydantic import BaseModel

class Sentiment(BaseModel):
    symbol: str
    sentiment_content: str
    content_timestamp: str
    sentiment_score: float | None = None