#!/usr/bin/env python3
"""
LCA Metals Prediction System - Launcher Script
"""

import subprocess
import sys
import os
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import streamlit
        import pandas
        import plotly
        import sklearn
        import joblib
        print("✅ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        return False

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.run([
            sys.executable, "-m", "pip", "install", 
            "-r", "streamlit_requirements.txt"
        ], check=True)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def check_models():
    """Check if model files exist"""
    models_dir = Path("models")
    if not models_dir.exists():
        print("⚠️  Warning: models directory not found!")
        print("Please ensure you have trained models in the models/ directory.")
        return False
    
    model_files = list(models_dir.glob("*.pkl"))
    if not model_files:
        print("⚠️  Warning: No model files found in models/ directory!")
        print("Please train and save models before running the app.")
        return False
    
    print(f"✅ Found {len(model_files)} model file(s)")
    for model_file in model_files:
        print(f"   📄 {model_file.name}")
    return True

def launch_app():
    """Launch the Streamlit application"""
    print("\n🚀 Launching LCA Metals Prediction System...")
    print("📱 Open your browser and go to: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the application")
    print("-" * 50)
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            "app/app.py", "--server.headless", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error launching app: {e}")

def main():
    """Main launcher function"""
    print("🌱 LCA Metals Prediction System Launcher")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        print("\n📦 Installing missing dependencies...")
        if not install_dependencies():
            print("❌ Cannot proceed without dependencies. Please install manually.")
            sys.exit(1)
    
    # Check models
    check_models()
    
    # Launch app
    launch_app()

if __name__ == "__main__":
    main()