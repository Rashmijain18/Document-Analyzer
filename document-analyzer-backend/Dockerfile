# ── Stage 1: base ───────────────────────────────────────────
FROM python:3.11-slim AS base

# Keeps Python from generating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering so logs appear instantly
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies needed by psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# ── Stage 2: dependencies ────────────────────────────────────
FROM base AS dependencies

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ── Stage 3: final ───────────────────────────────────────────
FROM dependencies AS final

# Copy app source
COPY . .

EXPOSE 8000

# Use --reload for dev (hot reload on file save)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
