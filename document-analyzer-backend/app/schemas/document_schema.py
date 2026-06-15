from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.document_model import DocumentStatus


# ── Response schema — what the API returns ──────────────────
class DocumentResponse(BaseModel):
    id:          int
    filename:    str
    file_type:   str
    file_size:   int
    status:      DocumentStatus
    page_count:  Optional[int]   = None
    chunk_count: Optional[int]   = None
    ai_cost:     Optional[str]   = None
    created_at:  datetime
    updated_at:  Optional[datetime] = None

    class Config:
        from_attributes = True   # lets pydantic read SQLAlchemy models directly


# ── List response — wraps a list with metadata ──────────────
class DocumentListResponse(BaseModel):
    total:     int
    documents: list[DocumentResponse]
