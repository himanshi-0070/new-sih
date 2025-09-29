#!/bin/bash

# Railway startup script for Streamlit
echo "🚀 Starting LCA-Mining Streamlit App on Railway..."

# Set default port if PORT is not set
if [ -z "$PORT" ]; then
    export PORT=8501
    echo "⚠️  PORT not set, using default: $PORT"
else
    echo "✅ Using PORT: $PORT"
fi

# Start Streamlit with proper port handling
echo "🌐 Starting Streamlit server on port $PORT..."
exec streamlit run app/app.py \
    --server.port=$PORT \
    --server.address=0.0.0.0 \
    --server.headless=true \
    --server.enableCORS=false \
    --server.enableXsrfProtection=false \
    --server.maxUploadSize=200