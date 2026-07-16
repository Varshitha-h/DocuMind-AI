from fastapi import APIRouter

from app.rag.retriever import Retriever
from app.schemas import ChatRequest, ChatResponse
from app.services.llm_service import LLMService

router = APIRouter()

retriever = Retriever()
llm = LLMService()


@router.post(
    "/chat",
    response_model=ChatResponse
)
async def chat(request: ChatRequest):
    """
    Ask a question about the uploaded document.
    """

    # Retrieve relevant document context
    context = retriever.retrieve(
        question=request.question
    )

    # Generate answer using the LLM
    answer = llm.generate_answer(
        question=request.question,
        context=context
    )

    return ChatResponse(
        question=request.question,
        answer=answer,
        context=context
    )