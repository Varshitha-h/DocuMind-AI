from fastapi import FastAPI

from app.api.upload import router as upload_router

app = FastAPI(
    title="DocuMind AI",
    description="LLM-powered Document Question Answering System",
    version="1.0.0"
)

app.include_router(upload_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to DocuMind AI 🚀"
    }