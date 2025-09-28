# LCA Metals Prediction System - Streamlit App

## Overview
This Streamlit application provides an interactive interface for predicting environmental and circularity indicators for metal production processes using machine learning.

## Features
- 🔮 **Predictive Analytics**: Predict environmental and circularity parameters
- 📊 **Interactive Visualizations**: Sankey diagrams, bar charts, and radar charts
- 🔄 **Pathway Comparison**: Compare Primary, Recycled, and Hybrid production pathways
- 💡 **Smart Recommendations**: Get actionable suggestions for improvement
- 📈 **Real-time Analysis**: Instant predictions and visualizations

## Quick Start

### 1. Install Dependencies
```bash
pip install -r streamlit_requirements.txt
```

### 2. Ensure Model is Available
Make sure you have a trained model file in one of these locations:
- `models/lca_model.pkl`
- `models/best_model.pkl`
- `models/final_optimized_lca_model.pkl`

### 3. Run the Application
```bash
streamlit run app/app.py
```

### 4. Access the App
Open your browser and go to: `http://localhost:8501`

## Application Structure

```
app/
├── app.py              # Main Streamlit application
├── plots.py            # Visualization functions
└── recommendations.py  # Recommendation engine
```

## How to Use

1. **Input Parameters**: Use the sidebar to input:
   - Metal type (Aluminum, Steel, Copper, etc.)
   - Process type (Primary, Secondary, Hybrid)
   - Transport distance, cost, and other parameters
   - Optional environmental data

2. **Generate Predictions**: Click "Generate Predictions" to get:
   - Environmental indicators (Energy, Emissions, Water)
   - Circularity indicators (Index, Recycled Content, Reuse Potential)

3. **View Comparisons**: Automatically see comparisons between different production pathways

4. **Explore Visualizations**:
   - Sankey diagram showing material flow
   - Bar charts for energy and emissions comparison
   - Radar chart for circularity metrics

5. **Get Recommendations**: Receive actionable suggestions for:
   - Environmental improvements
   - Circularity enhancements
   - Cost optimization

## Key Features

### 🎯 Prediction Capabilities
- Environmental impact assessment
- Circularity performance evaluation
- Multi-pathway comparison

### 📊 Visualizations
- **Sankey Diagram**: Material flow visualization
- **Bar Charts**: Energy and emissions comparison
- **Radar Chart**: Circularity metrics comparison
- **Summary Charts**: Overall performance overview

### 💡 Recommendation Engine
- **Environmental**: Energy efficiency, emission reduction, water conservation
- **Circularity**: Recycling, reuse, material recovery
- **Process-Specific**: Metal and process type recommendations
- **Technology**: Digital transformation and automation suggestions

## Configuration

The app automatically detects and loads trained models from the `models/` directory. Supported model formats:
- Scikit-learn models (via joblib)
- Multi-output regression models
- Custom model dictionaries

## Troubleshooting

### Model Loading Issues
- Ensure model file exists in `models/` directory
- Check model file format (should be .pkl)
- Verify model compatibility with current scikit-learn version

### Visualization Errors
- Install all required dependencies
- Check data format and structure
- Ensure predictions contain expected keys

### Performance Issues
- Reduce model complexity for faster predictions
- Optimize visualization parameters
- Use caching for repeated operations

## Technical Details

### Dependencies
- **Streamlit**: Web application framework
- **Plotly**: Interactive visualizations
- **Pandas/NumPy**: Data manipulation
- **Scikit-learn**: Machine learning models
- **Joblib**: Model serialization

### Model Requirements
The app expects models that predict these targets:
- `Energy_Use_MJ_per_kg`
- `Emission_kgCO2_per_kg`
- `Water_Use_l_per_kg`
- `Circularity_Index`
- `Recycled_Content_pct`
- `Reuse_Potential_score`

### Input Features
- `Metal`: Metal type (categorical)
- `Process_Type`: Production process (categorical)
- `End_of_Life`: End-of-life treatment (categorical)
- `Transport_km`: Transport distance (numerical)
- `Cost_per_kg`: Production cost (numerical)
- `Product_Life_Extension_years`: Product lifespan (numerical)
- `Waste_kg_per_kg_metal`: Waste ratio (numerical)

## Development

### Adding New Features
1. **New Visualizations**: Add functions to `plots.py`
2. **New Recommendations**: Extend `recommendations.py`
3. **UI Improvements**: Modify `app.py`

### Customization
- Modify color schemes in visualization functions
- Add new recommendation categories
- Extend input parameter options
- Customize styling with CSS

## Support

For issues or questions:
1. Check the console for error messages
2. Verify all dependencies are installed
3. Ensure model files are properly formatted
4. Check data input formats and ranges

---

🌱 **LCA Metals Prediction System** | Powered by Machine Learning & Streamlit