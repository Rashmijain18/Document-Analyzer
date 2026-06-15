from sqlalchemy import Column, Integer, String, DateTime, BigInteger, Enum
from sqlalchemy.sql import func
import enum
from app.database import Base


class DocumentStatus(str, enum.Enum):
    uploading   = "uploading"
    processing  = "processing"
    ready       = "ready"
    failed      = "failed"


class Document(Base):
    __tablename__ = "documents"

    id          = Column(Integer, primary_key=True, index=True)
    filename    = Column(String, nullable=False)           # original file name
    file_type   = Column(String, nullable=False)           # pdf, docx, etc
    file_size   = Column(BigInteger, nullable=False)       # bytes
    storage_url = Column(String, nullable=True)            # Azure Blob URL
    status      = Column(Enum(DocumentStatus), default=DocumentStatus.uploading)
    page_count  = Column(Integer, nullable=True)
    chunk_count = Column(Integer, nullable=True)           # how many vector chunks
    ai_cost     = Column(String, nullable=True)            # cost in USD string e.g. "0.04"
    created_at  = Column(DateTime(timezone=True), server_default=func.now())
    updated_at  = Column(DateTime(timezone=True), onupdate=func.now())
