@echo off
REM Activate virtual environment
.\venv\Scripts\Activate.ps1

REM Set environment variables to fix Streamlit + Torch conflicts
set STREAMLIT_WATCHER_TYPE=none
set KMP_DUPLICATE_LIB_OK=TRUE

REM Launch Streamlit app
streamlit run app.py

pause