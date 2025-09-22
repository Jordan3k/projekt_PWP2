
# syntax=docker/dockerfile:1
FROM python:3.13-slim

# Prevent Python from writing .pyc files & enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1         PYTHONUNBUFFERED=1         PIP_NO_CACHE_DIR=1

# Working directory
WORKDIR /app

# System deps (minimal; psycopg[binary] avoids libpq)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
&& rm -rf /var/lib/apt/lists/*

# Install Python deps first for better layer caching
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Create a non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

# Use gunicorn to serve Flask app (entrypoint defined in run.py as `app`)
CMD ["gunicorn", "-c", "gunicorn.conf.py", "run:app"]
