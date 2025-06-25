@echo off
:: ============================================================================
:: Ashley AI - Definitive Failsafe Launcher v2.0
:: This is the main entry point. It attempts to start the main application
:: and will automatically run the fallback launcher if the main one fails.
:: ============================================================================

:: Set the title of this console window
title Ashley AI Failsafe Launcher

echo --- Ashley AI Bootstrapper Initializing ---
echo.

:: --- Configuration ---
:: This assumes your full Python installation is in your system's PATH.
set "PYTHON_CMD=python"

:: --- Dynamic Path Setup ---
:: %~dp0 is the directory where this batch file is located (e.g., D:\AshleyAi\core\)
set "MAIN_APP=%~dp0ashley_failsafe.py"
set "FALLBACK_APP=%~dp0fallback_launcher.py"

:: --- Verification Stage ---
echo Verifying Python environment...
where %PYTHON_CMD% >nul 2>nul
if %errorlevel% neq 0 (
    echo [FATAL] Python was not found on your system or is not in the PATH.
    echo Please install Python from python.org and ensure "Add Python to PATH" is checked.
    echo.
    pause
    exit /b 1
)
echo [OK] Python environment found.
echo.

echo Verifying application files...
if not exist "%MAIN_APP%" (
    echo [FATAL] Main application '%MAIN_APP%' not found!
    pause
    exit /b 1
)
if not exist "%FALLBACK_APP%" (
    echo [FATAL] Fallback application '%FALLBACK_APP%' not found!
    pause
    exit /b 1
)
echo [OK] All application files are present.
echo.

:: --- Launch Stage ---
echo --- Attempting to launch Ashley's Main System... ---
echo --------------------------------------------------
echo.

:: This is the main command. We use start /wait to ensure this batch file
:: waits for the python process to finish before continuing.
start "Ashley Main System" /wait %PYTHON_CMD% "%MAIN_APP%"

:: This next part of the script will ONLY run if the python process above
:: has finished (either by closing normally or crashing).

:: Check the exit code of the last command.
:: A successful exit is typically code 0. Any other code indicates a failure/crash.
if %errorlevel% equ 0 (
    echo.
    echo --- Ashley's Main System exited normally. ---
    goto:end
)

:: --- Fallback Stage ---
echo.
echo [!!-FAILSAFE-!!] Main system failed to launch or crashed (Exit Code: %errorlevel%).
echo [!!-FAILSAFE-!!] Initiating fallback recovery launcher...
echo ------------------------------------------------------------
echo.

%PYTHON_CMD% "%FALLBACK_APP%"

:end
:: --- Shutdown Stage ---
echo.
echo -----------------------------------------
echo --- Ashley Failsafe session has concluded. ---
echo This window will remain open so you can review any messages.
pause
