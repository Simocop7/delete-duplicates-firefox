@echo off
echo 🚀 Installing Delete Duplicates Native Host...

REM Get the directory where this batch file is located
set "SCRIPT_DIR=%~dp0"
set "BACKEND_PATH=%SCRIPT_DIR%backend.py"

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is required but not installed.
    pause
    exit /b 1
)

REM Create the native messaging host manifest
set "NATIVE_HOST_DIR=%APPDATA%\Mozilla\NativeMessagingHosts"
if not exist "%NATIVE_HOST_DIR%" mkdir "%NATIVE_HOST_DIR%"

(
echo {
echo   "name": "com.deleteduplicates.python",
echo   "description": "Delete Duplicates Native Host",
echo   "path": "%BACKEND_PATH:\=\\%",
echo   "type": "stdio",
echo   "allowed_extensions": [
echo     "delete-duplicates@user"
echo   ]
echo }
) > "%NATIVE_HOST_DIR%\com.deleteduplicates.python.json"

echo ✅ Native host installed successfully!
echo 📁 Configuration file: %NATIVE_HOST_DIR%\com.deleteduplicates.python.json
echo 🐍 Backend script: %BACKEND_PATH%
echo.
echo Next steps:
echo 1. Open Firefox and go to about:debugging
echo 2. Click 'This Firefox' → 'Load Temporary Add-on'
echo 3. Select the manifest.json file from the extension folder
echo.
echo 📋 Test the installation:
echo    python "%BACKEND_PATH%" # Should wait for input (Ctrl+C to exit)
pause