# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install system dependencies (minimal set)
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Make scripts executable
RUN chmod +x start.sh start.py

# Create models directory if it doesn't exist
RUN mkdir -p models

# Note: Git LFS files will be handled by the robust fallback system
# No need to install git-lfs as we have demonstration models

# Expose port (Railway will set PORT env var)
EXPOSE $PORT

# Start command using Python startup script
CMD ["python", "start.py"]