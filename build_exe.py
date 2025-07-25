"""
Build script for KPI Analysis Pipeline
Automates the build process with proper error handling and cleanup
"""
import os
import sys
import shutil
import subprocess
from pathlib import Path

def run_command(cmd, description):
    """Run a command with proper error handling"""
    print(f"\n?? {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"? {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"? {description} failed:")
        print(f"Error: {e.stderr}")
        return False

def cleanup_old_builds():
    """Clean up previous builds"""
    dirs_to_clean = ["build", "dist"]
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            print(f"?? Cleaning up {dir_name}/")
            shutil.rmtree(dir_name)

def check_requirements():
    """Check if all required files exist"""
    required_files = ["main_pipeline.py", "setup.py"]
    missing_files = []

    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)

    if missing_files:
        print(f"? Missing required files: {', '.join(missing_files)}")
        return False

    print("? All required files found")
    return True

def install_requirements():
    """Install required packages"""
    packages = ["cx_Freeze"]

    # Try to read from requirements.txt
    if os.path.exists("requirements.txt"):
        with open("requirements.txt", "r") as f:
            packages.extend([line.strip() for line in f if line.strip() and not line.startswith("#")])

    for package in packages:
        if not run_command(f"pip install {package}", f"Installing {package}"):
            return False

    return True

def build_executable():
    """Build the executable using cx_Freeze"""
    return run_command("python setup.py build", "Building executable")

def build_installer():
    """Build Windows installer (MSI)"""
    if sys.platform == "win32":
        return run_command("python setup.py bdist_msi", "Building Windows installer")
    else:
        print("?? MSI installer only available on Windows")
        return True

def create_portable_package():
    """Create a portable package with all necessary files"""
    dist_dir = Path("dist/KPIAnalysisPipeline")
    portable_dir = Path("dist/KPIAnalysisPipeline_Portable")

    if dist_dir.exists():
        print("\n?? Creating portable package...")

        # Copy the built application
        if portable_dir.exists():
            shutil.rmtree(portable_dir)
        shutil.copytree(dist_dir, portable_dir)

        # Create a launcher script
        launcher_content = '''@echo off
echo Starting KPI Analysis Pipeline...
cd /d "%~dp0"
KPIAnalysisPipeline.exe
if errorlevel 1 (
    echo.
    echo Application encountered an error. Press any key to exit.
    pause >nul
)
'''

        with open(portable_dir / "Launch_KPI_Pipeline.bat", "w") as f:
            f.write(launcher_content)

        # Create README for portable version
        readme_content = '''# KPI Analysis Pipeline - Portable Version

## Quick Start
1. Double-click "Launch_KPI_Pipeline.bat" to start the application
2. Or run "KPIAnalysisPipeline.exe" directly

## Data Files
- Place your Excel/CSV files in the "data" folder
- Configuration is in "kpi_config.yaml"
- Generated reports will be in the "outputs" folder
- Logs are saved in the "logs" folder

## System Requirements
- Windows 10 or later
- No Python installation required (standalone)

## Support
- Check the logs folder for error details
- Ensure data files are properly formatted
- Contact support if issues persist

© AFIT BI 2025
'''

        with open(portable_dir / "README_PORTABLE.txt", "w") as f:
            f.write(readme_content)

        print("? Portable package created successfully")
        return True

    print("? Could not create portable package - build directory not found")
    return False

def main():
    """Main build process"""
    print("?? KPI Analysis Pipeline Build Script")
    print("=" * 50)

    # Check prerequisites
    if not check_requirements():
        sys.exit(1)

    # Clean up old builds
    cleanup_old_builds()

    # Install requirements
    print("\n?? Installing requirements...")
    if not install_requirements():
        print("? Failed to install requirements")
        sys.exit(1)

    # Build executable
    print("\n?? Building executable...")
    if not build_executable():
        print("? Failed to build executable")
        sys.exit(1)

    # Create portable package
    create_portable_package()

    # Build installer (Windows only)
    if sys.platform == "win32":
        print("\n?? Building Windows installer...")
        build_installer()

    # Final summary
    print("\n" + "=" * 50)
    print("?? Build completed successfully!")
    print("=" * 50)
    print("?? Generated files:")
    print("   - dist/KPIAnalysisPipeline/ (executable)")
    print("   - dist/KPIAnalysisPipeline_Portable/ (portable version)")
    if sys.platform == "win32":
        print("   - dist/*.msi (Windows installer)")

    print("\n?? Testing recommendations:")
    print("1. Test the executable on a clean machine")
    print("2. Verify all data files are processed correctly")
    print("3. Check that reports are generated properly")
    print("4. Test with different data file formats")

    print("\n?? Ready for distribution!")

if __name__ == "__main__":
    main()
