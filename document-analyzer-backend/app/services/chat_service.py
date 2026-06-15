from sqlalchemy.orm import Session
from fastapi import HTTPException, FastAPI, UploadFile, File
from typing import Optional
from pypdf import PdfReader
from io import BytesIO
from sentence_transformers import SentenceTransformer
from anthropic import Anthropic

from app.models.document_model import Document, DocumentStatus
from app.models.document_embedding import Document_Embedding


claude_client = Anthropic(api_key="your-anthropic-key")

class ChatService:
    """
    All business logic for documents lives here.
    The router calls this — it never touches the DB directly.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_response(
        self,
        document_id: int,
        question:    str
    ):
        # Check document exists
        document = db.query(Document).filter(Document.id == document_id).first()
        if not document:
            raise HTTPException(status_code=404, detail="Document not found")

        question_embedding = self.embedding(question)

        relevant_chunks= self.find_relevant_chunks(
            self,
            question_embedding
        )
        
        if not relevant_chunks:
            raise HTTPException(
                status_code=404,
                detail="No content found in this document to answer from"
        )

        prompt=self.build_prompt(relevant_chunks,question)

        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}]
        )

        # 3. Get the answer — one line
        answer = response.content[0].text

        return answer


    def embedding(text):
        model = SentenceTransformer("BAAI/bge-small-en-v1.5")

        embedding = model.encode(
            text,
            normalize_embeddings=True
        )
        return embedding

    def find_relevant_chunks(self,
        db: Session,
        question_vector: list[float],
        document_id: int,
        top_k: int = 5,
    ) -> list[str]:
        # query pgvector using cosine distance (<=>)
        # This finds the 5 chunks whose meaning is closest to the question
        chunks = (
            db.query(Document_Embedding)
            .filter(Document_Embedding.document_id == document_id)
            .order_by(Document_Embedding.embedding.cosine_distance(question_vector))
            .limit(top_k)
            .all()
        )
    
        return [chunk.content for chunk in chunks]
    
    def build_prompt(chunks: list[str], question: str) -> str:
        # Join all chunks into one context block
        context = "\n\n---\n\n".join(chunks)
    
        prompt = f"""You are a helpful assistant that answers questions about documents.
            Use ONLY the context below to answer the question.
            If the answer is not in the context, say "I couldn't find that in this document."
            Do not make up information.
    
            Context:
            {context}
            
            Question: {question}
            
            Answer:"""
 
        return prompt

