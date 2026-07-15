from fastapi import APIRouter, HTTPException
import logging
from pydantic import BaseModel
from fastapi import Request
from typing import List
#/api/v1/chat/

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/chat", tags=["Chat"])

class ChatRequest(BaseModel):
    message: str
    brand: str | None = None
    model: str | None = None
    year: int | None = None
    engine: str | None = None

    language: str = "en"

class SourceCitation(BaseModel):
    source: str
    brand: str | None = None
    model: str | None = None
    page: int | None = None

class ChatResponse(BaseModel):
    answer: str
    sources: List[SourceCitation]

@router.post("/", response_model=ChatResponse)
async def chat_with_meister(payload: ChatRequest,request:Request):
    try:  
        # 3. Generate response using LLM (OpenAI/Gemini/Ollama)     
        assistant = request.app.state.assistant
        answer, docs = assistant.ask(payload.message)
        sources = []

        for doc in docs:

            meta = doc["metadata"]

            sources.append(
                SourceCitation(
                    source=meta["manual"],
                    brand=meta.get("brand"),
                    model=meta.get("model"),
                    page=meta.get("page")
                )
            ) 
            
        # Deduplicate sources based on document name/page
        unique = {}

        for source in sources:

            key = (source.source, source.page)

            unique[key] = source
        # unique_sources = {f"{s.source}_{s.page}": s for s in sources}.values()

        # 3. Generate response using LLM (OpenAI/Gemini/Ollama)
        # answer = generate_answer(question=payload.message, context=context_text)
 

        return ChatResponse(answer=answer, sources=list(unique.values()))

    except Exception as e:
        logger.exception("RAG Generation failed")

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )