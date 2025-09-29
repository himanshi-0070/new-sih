#!/bin/bash

# Git LFS Setup Script for Railway Deployment
echo "🔧 Setting up Git LFS for Railway deployment..."

# Check if git lfs is available
if command -v git-lfs &> /dev/null; then
    echo "✅ Git LFS is available"
    
    # Initialize Git LFS
    git lfs install
    
    # Pull LFS files
    echo "📥 Pulling Git LFS files..."
    git lfs pull
    
    # Check if model files exist and are not LFS pointers
    echo "🔍 Checking model files..."
    
    if [ -d "models" ]; then
        for file in models/*.pkl; do
            if [ -f "$file" ]; then
                # Check if file is a Git LFS pointer
                if head -c 200 "$file" | grep -q "version https://git-lfs.github.com"; then
                    echo "⚠️  $file is still a Git LFS pointer"
                else
                    echo "✅ $file appears to be a valid model file"
                fi
            fi
        done
    else
        echo "⚠️  Models directory not found"
    fi
else
    echo "⚠️  Git LFS not available - model files may not load properly"
    echo "💡 The application will use fallback demonstration models"
fi

echo "🎉 Git LFS setup completed"