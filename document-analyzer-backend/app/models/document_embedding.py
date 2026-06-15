from sqlalchemy import Column, Integer, String, DateTime, BigInteger, Enum
from sqlalchemy.sql import func
from pgvector.sqlalchemy import Vector
from app.database import Base


class Document_Embedding(Base):
    __tablename__ = "document_embeddings"

    id              = Column(Integer, primary_key=True, index=True)
    document_id     = Column(Integer, nullable=False)  
    chunk_text      = Column(String, nullable=False)
    embedding       = Column(Vector(384), nullable=False)         
    created_at  = Column(DateTime(timezone=True), server_default=func.now())
    updated_at  = Column(DateTime(timezone=True), onupdate=func.now())
