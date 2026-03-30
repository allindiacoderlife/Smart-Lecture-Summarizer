from fastapi import APIRouter
from pydantic import BaseModel
from services.chatbot import get_response

router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@router.post("/chat")
def chat(req: ChatRequest):
    answer = get_response(req.question)
    return {"answer": answer}
