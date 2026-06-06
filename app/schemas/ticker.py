from pydantic import BaseModel

class Ticker(BaseModel):
    symbol: str
    stock_name: str
    description: str | None = None
    current_price: float | None = None
    last_updated: str | None = None