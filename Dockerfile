# ----- STAGE 1: Build dependencies -----
FROM python:3.10-slim AS builder

WORKDIR /app

# System deps for building some Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


# ----- STAGE 2: Runtime image -----
FROM python:3.10-slim

WORKDIR /app

# Copy Python deps from builder
COPY --from=builder /usr/local /usr/local

# Copy application code
COPY . .

EXPOSE 8001

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]