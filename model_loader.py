"""
Robust Model Loading System for Railway Deployment
Handles Git LFS issues and provides fallback mechanisms
"""

import joblib
import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from pathlib import Path
import requests
import os
import streamlit as st

class ModelLoader:
    """Robust model loader with fallback mechanisms"""
    
    def __init__(self):
        self.model_paths = [
            Path("models/corrected_optimized_dual_target_model.pkl"),
            Path("../models/corrected_optimized_dual_target_model.pkl"),
            Path("models/clean_optimized_dual_target_model.pkl"),
            Path("../models/clean_optimized_dual_target_model.pkl"),
            Path("models/lca_model.pkl"),
            Path("../models/lca_model.pkl")
        ]
    
    def check_git_lfs_files(self):
        """Check if Git LFS files are properly downloaded"""
        lfs_indicators = ['version https://git-lfs.github.com', 'oid sha256:', 'size ']
        
        for model_path in self.model_paths:
            if model_path.exists():
                try:
                    # Check first few lines to see if it's a Git LFS pointer
                    with open(model_path, 'rb') as f:
                        first_bytes = f.read(200).decode('utf-8', errors='ignore')
                        if any(indicator in first_bytes for indicator in lfs_indicators):
                            st.warning(f"⚠️ {model_path.name} appears to be a Git LFS pointer, not actual model file")
                            return False
                except:
                    continue
        return True
    
    def download_fallback_model(self):
        """Download a minimal working model if main models fail"""
        try:
            st.info("📥 Downloading fallback model...")
            # This would normally download from a backup source
            # For now, we'll create a minimal model
            return self.create_minimal_model()
        except Exception as e:
            st.error(f"Failed to download fallback model: {e}")
            return None
    
    def create_minimal_model(self):
        """Create a minimal working model for demonstration"""
        st.info("🔧 Creating minimal demonstration model...")
        
        try:
            # Create synthetic training data matching the expected format
            np.random.seed(42)
            n_samples = 1000
            
            # Generate synthetic features
            X = np.random.rand(n_samples, 13)  # 13 features as expected
            
            # Generate synthetic targets (6 outputs)
            y = np.random.rand(n_samples, 6)
            y[:, 0] = X[:, 0] * 100 + np.random.normal(0, 10, n_samples)  # Energy
            y[:, 1] = X[:, 1] * 20 + np.random.normal(0, 2, n_samples)   # Emissions
            y[:, 2] = X[:, 2] * 50 + np.random.normal(0, 5, n_samples)   # Water
            y[:, 3] = np.clip(X[:, 3], 0, 1)  # Circularity Index
            y[:, 4] = X[:, 4] * 100  # Recycled Content
            y[:, 5] = np.clip(X[:, 5], 0, 1)  # Reuse Potential
            
            # Train a simple model
            model = RandomForestRegressor(n_estimators=10, random_state=42)
            model.fit(X, y)
            
            # Create model data structure
            model_data = {
                'model': model,
                'model_type': 'fallback_minimal',
                'metadata': {
                    'model_version': '1.0.0-fallback',
                    'feature_alignment': 'corrected',
                    'features_count': 13,
                    'target_names': [
                        'Energy_Use_MJ_per_kg',
                        'Emission_kgCO2_per_kg', 
                        'Water_Use_l_per_kg',
                        'Circularity_Index',
                        'Recycled_Content_pct',
                        'Reuse_Potential_score'
                    ]
                },
                'feature_names': [
                    'Transport_km', 'Cost_per_kg', 'Product_Life_Extension_years',
                    'Waste_kg_per_kg_metal', 'Energy_per_km', 'Energy_per_cost',
                    'Emission_per_energy', 'Waste_ratio', 'Cost_efficiency',
                    'Transport_efficiency', 'Metal_Aluminum', 'Process_Primary', 'EndLife_Recycled'
                ]
            }
            
            st.success("✅ Minimal demonstration model created successfully")
            st.info("📝 Note: This is a demonstration model. For production use, please ensure proper model files are available.")
            
            return model_data
            
        except Exception as e:
            st.error(f"Failed to create minimal model: {e}")
            return None
    
    def load_model_file(self, model_path):
        """Load a single model file with error handling"""
        try:
            # Try pickle first (for newer models)
            if "optimized_dual_target" in model_path.name:
                with open(model_path, 'rb') as f:
                    return pickle.load(f)
            else:
                return joblib.load(model_path)
        except Exception as e:
            st.error(f"Error loading {model_path.name}: {str(e)}")
            return None
    
    def load(self):
        """Main model loading method with fallback chain"""
        try:
            # Check if Git LFS files are properly downloaded
            if not self.check_git_lfs_files():
                st.warning("⚠️ Git LFS files may not be properly downloaded")
            
            # Try to load existing models
            for model_path in self.model_paths:
                if model_path.exists():
                    st.info(f"🔍 Attempting to load: {model_path.name}")
                    
                    model_data = self.load_model_file(model_path)
                    if model_data is not None:
                        st.success(f"✅ Model loaded successfully from {model_path.name}")
                        
                        # Display model information
                        if isinstance(model_data, dict) and 'model_type' in model_data:
                            st.info(f"📊 Model Type: {model_data['model_type']}")
                            if 'metadata' in model_data:
                                metadata = model_data['metadata']
                                st.info(f"🔢 Version: {metadata.get('model_version', 'Unknown')}")
                                st.success(f"✅ Feature Alignment: {metadata.get('feature_alignment', 'Unknown')}")
                                st.info(f"🔧 Expected Features: {metadata.get('features_count', 'Unknown')}")
                        
                        return model_data
            
            # If no models found or all failed, use fallback
            st.warning("⚠️ No valid model files found. Creating fallback model...")
            return self.create_minimal_model()
            
        except Exception as e:
            st.error(f"❌ Critical error in model loading: {str(e)}")
            st.info("🔧 Attempting to create fallback model...")
            return self.create_minimal_model()

# Global model loader instance
_model_loader = ModelLoader()

@st.cache_resource
def load_robust_model():
    """Cached model loading with robust fallback"""
    return _model_loader.load()