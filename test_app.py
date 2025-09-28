"""
Test script for LCA Streamlit App
"""

import sys
import os
from pathlib import Path

# Add app directory to path
sys.path.append(str(Path(__file__).parent / "app"))

def test_imports():
    """Test if all required modules can be imported"""
    print("🧪 Testing imports...")
    
    try:
        import streamlit as st
        print("✅ Streamlit import successful")
    except ImportError as e:
        print(f"❌ Streamlit import failed: {e}")
        return False
    
    try:
        from app.plots import create_sankey_diagram, create_energy_comparison
        print("✅ Plots module import successful")
    except ImportError as e:
        print(f"❌ Plots module import failed: {e}")
        return False
    
    try:
        from app.recommendations import get_environmental_recommendations
        print("✅ Recommendations module import successful")
    except ImportError as e:
        print(f"❌ Recommendations module import failed: {e}")
        return False
    
    return True

def test_model_loading():
    """Test model loading functionality"""
    print("\n🔍 Testing model loading...")
    
    import joblib
    from pathlib import Path
    
    models_dir = Path("models")
    if not models_dir.exists():
        print("❌ Models directory not found")
        return False
    
    model_files = list(models_dir.glob("*.pkl"))
    if not model_files:
        print("❌ No model files found")
        return False
    
    try:
        model_path = model_files[0]  # Use first available model
        model_data = joblib.load(model_path)
        print(f"✅ Model loaded from {model_path.name}")
        
        # Test model structure
        if isinstance(model_data, dict):
            if 'model' in model_data:
                print("✅ Model dictionary structure is correct")
            else:
                print("⚠️  Model dictionary missing 'model' key")
        
        return True
    except Exception as e:
        print(f"❌ Model loading failed: {e}")
        return False

def test_predictions():
    """Test prediction functionality"""
    print("\n🔮 Testing predictions...")
    
    try:
        # Sample input data
        sample_input = {
            'Metal': 0,
            'Process_Type': 1,
            'End_of_Life': 0,
            'Transport_km': 500.0,
            'Cost_per_kg': 5.0,
            'Product_Life_Extension_years': 10.0,
            'Waste_kg_per_kg_metal': 0.3
        }
        
        import pandas as pd
        import joblib
        from pathlib import Path
        
        # Load model
        model_files = list(Path("models").glob("*.pkl"))
        if model_files:
            model_data = joblib.load(model_files[0])
            
            # Extract model
            if isinstance(model_data, dict) and 'model' in model_data:
                model = model_data['model']
            else:
                model = model_data
            
            # Make prediction
            input_df = pd.DataFrame([sample_input])
            predictions = model.predict(input_df) # type: ignore
            
            print("✅ Prediction successful")
            print(f"   Prediction shape: {predictions.shape}")
            
            return True
        else:
            print("❌ No model files available for testing")
            return False
            
    except Exception as e:
        print(f"❌ Prediction test failed: {e}")
        return False

def test_visualizations():
    """Test visualization functions"""
    print("\n📊 Testing visualizations...")
    
    try:
        from app.plots import create_sankey_diagram
        
        # Sample prediction data
        sample_predictions = {
            'Energy_Use_MJ_per_kg': 120.0,
            'Emission_kgCO2_per_kg': 8.5,
            'Water_Use_l_per_kg': 45.0,
            'Circularity_Index': 0.35,
            'Recycled_Content_pct': 25.0,
            'Reuse_Potential_score': 0.6
        }
        
        # Test Sankey diagram creation
        fig = create_sankey_diagram(sample_predictions)
        print("✅ Sankey diagram creation successful")
        
        return True
    except Exception as e:
        print(f"❌ Visualization test failed: {e}")
        return False

def test_recommendations():
    """Test recommendation functions"""
    print("\n💡 Testing recommendations...")
    
    try:
        from app.recommendations import get_environmental_recommendations, get_circularity_recommendations
        
        # Sample prediction data
        sample_predictions = {
            'Energy_Use_MJ_per_kg': 120.0,
            'Emission_kgCO2_per_kg': 8.5,
            'Water_Use_l_per_kg': 45.0,
            'Circularity_Index': 0.35,
            'Recycled_Content_pct': 25.0,
            'Reuse_Potential_score': 0.6
        }
        
        # Test environmental recommendations
        env_recs = get_environmental_recommendations(sample_predictions)
        print(f"✅ Environmental recommendations: {len(env_recs)} items")
        
        # Test circularity recommendations
        circ_recs = get_circularity_recommendations(sample_predictions)
        print(f"✅ Circularity recommendations: {len(circ_recs)} items")
        
        return True
    except Exception as e:
        print(f"❌ Recommendations test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 LCA Streamlit App Test Suite")
    print("=" * 40)
    
    tests = [
        ("Imports", test_imports),
        ("Model Loading", test_model_loading),
        ("Predictions", test_predictions),
        ("Visualizations", test_visualizations),
        ("Recommendations", test_recommendations)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n📋 TEST RESULTS SUMMARY:")
    print("=" * 30)
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("\n🎊 All tests passed! Streamlit app is ready to launch.")
        print("Run: streamlit run app/app.py")
    else:
        print(f"\n⚠️  {len(tests) - passed} test(s) failed. Please check the issues above.")

if __name__ == "__main__":
    main()