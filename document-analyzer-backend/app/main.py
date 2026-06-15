from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.api.documents import router as documents_router
from app.models.document_model import Document  # ← add this line

# Create all tables on startup (fine for dev — use Alembic for production)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DocMind API",
    version="0.1.0",
    description="AI Document Intelligence Platform",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(documents_router, prefix="/api/v1")


@app.get("/health")
def health():
    return {"status": "ok", "version": "0.1.0"}
