@echo off
echo Starting FleTodo - Simple Todo List Application...
echo.

REM Change to the directory containing this script
cd /d "%~dp0"

REM Run the FleTodo application
start "" "FleTodo\FleTodo.exe"

REM If there was an error, pause to show it
if errorlevel 1 (
    echo.
    echo Error starting FleTodo. Please check the executable file.
    pause
)
