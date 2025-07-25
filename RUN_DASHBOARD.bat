@echo off
echo ========================================
echo    DOGANHUB - DASHBOARD
echo ========================================
echo.

cd /d "d:\DoganLab"

echo Starting DoganHub Dashboard...
echo Open browser to: http://localhost:8501
echo.
streamlit run DoganHub_SIMPLE.py dashboard

pause
