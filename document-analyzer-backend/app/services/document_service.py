from sqlalchemy.orm import Session
from fastapi import HTTPException, FastAPI, UploadFile, File
from typing import Optional
from pypdf import PdfReader
from io import BytesIO
from sentence_transformers import SentenceTransformer

from app.models.document_model import Document, DocumentStatus
from app.models.document_embedding import Document_Embedding

class DocumentService:
    """
    All business logic for documents lives here.
    The router calls this — it never touches the DB directly.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_all(
        self,
        status: Optional[DocumentStatus] = None,
        page: int = 1,
        per_page: int = 10,
    ) -> tuple[int, list[Document]]:
        query = self.db.query(Document)

        if status:
            query = query.filter(Document.status == status)

        total = query.count()
        documents = (
            query
            .order_by(Document.created_at.desc())
            .offset((page - 1) * per_page)
            .limit(per_page)
            .all()
        )
        return total, documents

    async def process_document(
            self,
            file: UploadFile
    ):
        pdf_bytes = await file.read()
        filename = file.filename
        content_type = file.content_type
        size = len(pdf_bytes)
        content = self.extract_text(self, pdf_bytes)
        chunks = self.chunk_content(content)
        document = Document(
            filename=filename,
            file_type=content_type,
            file_size=size,
            status=DocumentStatus.processing,
            page_count=None,
            chunk_count=None,
            ai_cost=None,
        )
        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)

        for chunk in chunks:
            embedding = self.embedding(chunk)
            document_embedding = Document_Embedding(
                document_id = document.id
                chunk_text = chunk
                embedding = embedding
            )
            self.db.add(document_embedding)
            self.db.commit()
            self.db.refresh(document_embedding)
        return

    def extract_text(self,pdfbytes):
        reader = PdfReader(BytesIO(pdfbytes))
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text
    
    def chunk_content(content):
        chunk_size = 1000
        overlap = 50
        current_chunk_index=0
        chunks=[]
        content_len=len(content)
        while(current_chunk_index<content_len):
            if current_chunk_index+chunk_size+overlap>content_len:
                chunks.append(content[current_chunk_index:])
            elif current_chunk_index == 0:
                chunks.append(content[current_chunk_index:current_chunk_index+chunk_size])
            else: 
                chunks.append(content[current_chunk_index-overlap:current_chunk_index+chunk_size])
            current_chunk_index=current_chunk_index+chunk_size
        return chunks
    
    def embedding(text):
        model = SentenceTransformer("BAAI/bge-small-en-v1.5")

        embedding = model.encode(
            text,
            normalize_embeddings=True
        )

        return embedding

