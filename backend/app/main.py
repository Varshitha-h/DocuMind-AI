from fastapi import FastAPI

app = FastAPI(
    title="DocuMind AI",
    description="LLM-powered Document Question Answering System",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to DocuMind AI 🚀"
    }

