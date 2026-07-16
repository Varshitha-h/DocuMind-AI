from fastapi import FastAPI

from app.api.upload import router as upload_router
from app.api.chat import router as chat_router

app = FastAPI(
    title="DocuMind AI",
    description="LLM-powered Document Question Answering System",
    version="1.0.0"
)

app.include_router(upload_router)
app.include_router(chat_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to DocuMind AI 🚀"
    }