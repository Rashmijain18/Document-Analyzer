from fastapi import APIRouter, Depends, Query, FastAPI, UploadFile, File
from sqlalchemy.orm import Session
from typing import Optional

from app.database import get_db
from app.models.document_model import DocumentStatus
from app.schemas.document_schema import DocumentResponse, DocumentListResponse
from app.services.document_service import DocumentService
from app.services.chat_service import ChatService
from app.schemas.chat_schema import AnswerResponse

router = APIRouter(prefix="/chat", tags=["Chat"])


# ── GET /documents ───────────────────────────────────────────
@router.post("/{document_id}/ask", response_model=AnswerResponse)
def chat(
    document_id: Integer,
    question:    String,
    db:          Session = Depends(get_db),
):
    # Router only handles HTTP concerns — delegates to service
    service = ChatService(db)
    response = service.get_response(document_id, question)
    return response

