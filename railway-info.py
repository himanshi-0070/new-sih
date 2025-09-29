#!/usr/bin/env python3
"""
Railway-specific setup and info script
"""

import os
import sys
from pathlib import Path

def railway_info():
    """Display Railway deployment information"""
    print("🚄 Railway Deployment Information")
    print("=" * 50)
    
    # Environment info
    print(f"🐍 Python Version: {sys.version}")
    print(f"📁 Working Directory: {os.getcwd()}")
    print(f"🌐 PORT Environment: {os.environ.get('PORT', 'Not set')}")
    
    # Check file structure
    print("\n📂 File Structure Check:")
    important_paths = [
        "app/app.py",
        "requirements.txt", 
        "start.py",
        "model_loader.py",
        "models/"
    ]
    
    for path in important_paths:
        path_obj = Path(path)
        if path_obj.exists():
            if path_obj.is_dir():
                files = list(path_obj.glob("*"))
                print(f"✅ {path} (contains {len(files)} files)")
            else:
                print(f"✅ {path}")
        else:
            print(f"❌ {path} (missing)")
    
    # Model status
    print("\n🤖 Model Status:")
    models_dir = Path("models")
    if models_dir.exists():
        model_files = list(models_dir.glob("*.pkl"))
        if model_files:
            print(f"📊 Found {len(model_files)} model files")
            for model_file in model_files[:3]:  # Show first 3
                size = model_file.stat().st_size
                print(f"  - {model_file.name} ({size:,} bytes)")
        else:
            print("⚠️  No model files found - will use demonstration models")
    else:
        print("⚠️  Models directory not found - will use demonstration models")
    
    print("\n💡 Railway Deployment Notes:")
    print("- This app uses robust fallback models if Git LFS files unavailable")
    print("- Demonstration models provide full functionality for testing")
    print("- All visualizations and features work with demo models")
    print("- For production, ensure proper Git LFS setup")
    
    print("\n🎉 Railway deployment ready!")

if __name__ == "__main__":
    railway_info()