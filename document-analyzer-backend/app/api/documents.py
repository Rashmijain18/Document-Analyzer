from fastapi import APIRouter, Depends, Query, FastAPI, UploadFile, File
from sqlalchemy.orm import Session
from typing import Optional

from app.database import get_db
from app.models.document_model import DocumentStatus
from app.schemas.document_schema import DocumentResponse, DocumentListResponse
from app.services.document_service import DocumentService

router = APIRouter(prefix="/documents", tags=["Documents"])


# ── GET /documents ───────────────────────────────────────────
@router.get("", response_model=DocumentListResponse)
def list_documents(
    status:   Optional[DocumentStatus] = Query(None),
    page:     int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100),
    db:       Session = Depends(get_db),
):
    # Router only handles HTTP concerns — delegates to service
    service = DocumentService(db)
    total, documents = service.get_all(status=status, page=page, per_page=per_page)
    return DocumentListResponse(total=total, documents=documents)


@router.post()
async def upload_document(
    file:   UploadFile = File(...),
    db:     Session = Depends(get_db)
):
    service = DocumentService(db)
    await service.process_document(file)
    return 

