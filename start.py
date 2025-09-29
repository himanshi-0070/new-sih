#!/usr/bin/env python3
"""
Railway Streamlit Startup Script
Handles PORT environment variable properly for Railway deployment
"""

import os
import subprocess
import sys

def main():
    print("🚀 Starting LCA-Mining Streamlit App on Railway...")
    
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