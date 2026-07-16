from pydantic import BaseModel
from fastapi import APIRouter

from app.rag.retriever import Retriever
from app.services.llm_service import LLMService

router = APIRouter()

retriever = Retriever()
llm = LLMService()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(request: ChatRequest):
    """
    Ask a question about the uploaded document.
    """

    # Retrieve relevant context
    context = retriever.retrieve(
        question=request.question
    )

    # Generate answer using Llama
    answer = llm.generate_answer(
        question=request.question,
        context=context
    )

    return {
        "question": request.question,
        "answer": answer,
        "context": context
    }