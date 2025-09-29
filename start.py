#!/usr/bin/env python3
"""
Railway Streamlit Startup Script
Handles PORT environment variable and model checking for Railway deployment
"""

import os
import subprocess
import sys
from pathlib import Path

def check_models():
    """Check if model files are available and valid"""
    print("🔍 Checking model files...")
    
    models_dir = Path("models")
    if not models_dir.exists():
        print("⚠️  Models directory not found - application will use fallback models")
        return False
    
    model_files = list(models_dir.glob("*.pkl"))
    if not model_files:
        print("⚠️  No model files found - application will use fallback models")
        return False
    
    # Check if files are Git LFS pointers
    lfs_indicators = [b'version https://git-lfs.github.com', b'oid sha256:', b'size ']
    
    for model_file in model_files:
        try:
            with open(model_file, 'rb') as f:
                first_bytes = f.read(200)
                if any(indicator in first_bytes for indicator in lfs_indicators):
                    print(f"⚠️  {model_file.name} appears to be a Git LFS pointer")
                    print("💡 Application will create fallback demonstration models")
                    return False
                else:
                    print(f"✅ {model_file.name} appears to be a valid model file")
        except Exception as e:
            print(f"⚠️  Could not read {model_file.name}: {e}")
    
    return True

def main():
    print("🚀 Starting LCA-Mining Streamlit App on Railway...")
    
    # Check model files
    models_available = check_models()
    if models_available:
        print("✅ Model files are available")
    else:
        print("💡 Will use demonstration models with synthetic data")
    
    # Get port from environment, default to 8501
    port = os.environ.get('PORT', '8501')
    print(f"✅ Using PORT: {port}")
    
    # Validate port is numeric
    try:
        port_int = int(port)
        if port_int < 1 or port_int > 65535:
            raise ValueError("Port out of range")
    except ValueError:
        print(f"❌ Invalid PORT value: {port}, using default 8501")
        port = '8501'
    
    # Build streamlit command
    cmd = [
        sys.executable, '-m', 'streamlit', 'run', 'app/app.py',
        '--server.port', port,
        '--server.address', '0.0.0.0',
        '--server.headless', 'true',
        '--server.enableCORS', 'false',
        '--server.enableXsrfProtection', 'false',
        '--server.maxUploadSize', '200'
    ]
    
    print(f"🌐 Starting Streamlit server on port {port}...")
    print(f"Command: {' '.join(cmd)}")
    
    # Execute streamlit
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Streamlit failed to start: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("👋 Streamlit stopped by user")
        sys.exit(0)

if __name__ == '__main__':
    main()