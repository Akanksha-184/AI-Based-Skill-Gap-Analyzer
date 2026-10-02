from fastapi import APIRouter, HTTPException
from models.api_models import ChatRequest, ChatResponse
from services.ai_service import get_chat_response

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_with_assistant(request: ChatRequest):
    try:
        reply = await get_chat_response(request.messages, request.context)
        return ChatResponse(reply=reply)
    except Exception as e:
        print(f"Error in chat_with_assistant: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while chatting with the assistant.")
