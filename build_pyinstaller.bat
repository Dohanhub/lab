@echo off
echo Building KPI Analysis Pipeline with PyInstaller...
echo.

:: Install PyInstaller if not present
pip install pyinstaller

:: Clean previous builds
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"

:: Build using spec file
pyinstaller KPIAnalysisPipeline.spec

:: Check if build was successful
if exist "dist\KPIAnalysisPipeline\KPIAnalysisPipeline.exe" (
    echo.
    echo ✅ Build completed successfully!
    echo 📁 Output: dist\KPIAnalysisPipeline\
    echo.
    echo To test: cd dist\KPIAnalysisPipeline && KPIAnalysisPipeline.exe
) else (
    echo.
    echo ❌ Build failed! Check the output above for errors.
)
pause
