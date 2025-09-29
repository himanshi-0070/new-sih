#!/bin/bash

# Railway deployment script
echo "🚀 Starting Railway deployment for LCA-Mining..."

# Upgrade pip and install dependencies
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# Verify Streamlit installation
python -c "import streamlit; print(f'✅ Streamlit {streamlit.__version__} installed')"

# Check if models exist
if [ -d "models" ]; then
    echo "✅ Models directory found"
    ls -la models/
else
    echo "⚠️  Models directory not found - creating placeholder"
    mkdir -p models
fi

echo "🎉 Railway build completed successfully!"