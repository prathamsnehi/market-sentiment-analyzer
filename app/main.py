from fastapi import FastAPI
from api.v1.api import api_router

app = FastAPI(
    title="My FastAPI",
    description="My FastAPI Description",
    version="1.0.0",
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
def get_health():
    return {"status": "ok"}