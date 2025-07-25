@echo off
echo Building KPI Analysis Pipeline as single file...
echo.

:: Install PyInstaller if not present
pip install pyinstaller

:: Clean previous builds
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"

:: Build as single file (slower startup but easier distribution)
pyinstaller --onefile --windowed --icon=assets/icon.ico --name=KPIAnalysisPipeline main_pipeline.py

:: Add data files manually to the same directory
if exist "dist\KPIAnalysisPipeline.exe" (
    if exist "kpi_config.yaml" copy "kpi_config.yaml" "dist\"
    if exist "data" xcopy "data" "dist\data\" /e /i /y
    if exist "templates" xcopy "templates" "dist\templates\" /e /i /y
    echo.
    echo ✅ Single file build completed!
    echo 📁 Output: dist\KPIAnalysisPipeline.exe
    echo.
    echo Note: Place your data files in the same directory as the .exe
) else (
    echo.
    echo ❌ Build failed! Check the output above for errors.
)
pause
