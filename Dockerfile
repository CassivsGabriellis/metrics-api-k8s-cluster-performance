# Small Python image
FROM python:3.12-slim AS base

# Set Python to run in unbuffered mode (better logs) and disable .pyc
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# Install system dependencies (psutil may need gcc and linux headers)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        build-essential \
        && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app ./app

# Expose the port used by the API
EXPOSE 8000

# Default environment variables
ENV APP_ENV=prod

# Command to run the application
# Using uvicorn with FastAPI app at app.main:app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]