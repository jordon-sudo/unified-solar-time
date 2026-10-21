@echo off
REM Unified Solar Time (UST) Clock - Build Script for Windows
REM This script creates a standalone .exe file

echo Building Unified Solar Time (UST) Clock...
echo.

REM Check if pyinstaller is installed
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo Installing PyInstaller...
    pip install pyinstaller
)

echo.
echo Creating executable...
pyinstaller --onefile --windowed --name "Unified Solar Time" --icon=NONE ust_clock.py

echo.
echo Build complete!
echo.
echo Your executable is located at:
echo   dist\Unified Solar Time.exe
echo.
echo Copy it anywhere and double-click to run!
pause
