@echo off
echo Starting LCA Metals Prediction System...
echo.

REM Check if streamlit is installed
python -c "import streamlit" 2>nul
if %errorlevel% neq 0 (
    echo Streamlit not found. Installing dependencies...
    pip install -r streamlit_requirements.txt
    echo.
)

REM Check if models directory exists
if not exist "models" (
    echo Warning: models directory not found!
    echo Please ensure you have trained models in the models/ directory.
    echo.
)

REM Start the Streamlit app
echo Launching Streamlit app...
echo Open your browser and go to: http://localhost:8501
echo.
streamlit run app/app.py

pause