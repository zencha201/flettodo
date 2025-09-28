#!/usr/bin/env python3
"""
Build script for FleTodo Windows Application
Creates a Windows executable version of the Flet todo app.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

def create_windows_build():
    """Create the Windows build using Flet's build command."""
    
    # Get project directory
    project_dir = Path(__file__).parent
    build_dir = project_dir / "bin" / "win"
    
    print("🚀 Building FleTodo for Windows...")
    print(f"📁 Project directory: {project_dir}")
    print(f"📦 Build directory: {build_dir}")
    
    # Create bin/win directory
    build_dir.mkdir(parents=True, exist_ok=True)
    
    # Clean existing build directory contents
    if build_dir.exists() and any(build_dir.iterdir()):
        print("🧹 Cleaning existing build directory...")
        for item in build_dir.iterdir():
            if item.is_file():
                item.unlink()
            elif item.is_dir():
                shutil.rmtree(item)
    
    # Build command for Windows executable
    build_cmd = [
        "flet", "build", "windows",
        str(project_dir / "main.py"),
        "--output", str(build_dir),
        "--project", "FleTodo",
        "--description", "A simple and elegant todo list application built with Flet",
        "--product", "FleTodo",
        "--company", "FleTodo Team",
        "--copyright", "Copyright (c) 2025 FleTodo Team",
        "--build-version", "1.0.0"
    ]
    
    print("⚙️  Running Flet build command...")
    print(f"   Command: {' '.join(build_cmd)}")
    
    try:
        result = subprocess.run(build_cmd, cwd=project_dir, check=True, capture_output=True, text=True)
        print("✅ Build completed successfully!")
        
        if result.stdout:
            print("📋 Build output:")
            print(result.stdout)
            
        # Create documentation and scripts
        create_windows_readme(build_dir)
        create_run_script(build_dir)
        report_build_results(build_dir)
        return True
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed with exit code {e.returncode}")
        if e.stdout:
            print("📋 Build output:")
            print(e.stdout)
        if e.stderr:
            print("🚨 Build errors:")
            print(e.stderr)
        print("⚡ Trying alternative pack method...")
    
    # Try alternative pack method if build fails or for standalone executable
    print("\n🎯 Creating standalone executable with flet pack...")
    
    pack_cmd = [
        "flet", "pack",
        str(project_dir / "main.py"),
        "--name", "FleTodo",
        "--distpath", str(build_dir),
        "--product-name", "FleTodo",
        "--file-description", "FleTodo - Simple Todo List Application",
        "--product-version", "1.0.0",
        "--company-name", "FleTodo Team",
        "--copyright", "Copyright (c) 2025 FleTodo Team",
        "--onedir"  # Create one-folder bundle
    ]
    
    print(f"   Pack Command: {' '.join(pack_cmd)}")
    
    try:
        result = subprocess.run(pack_cmd, cwd=project_dir, check=True, capture_output=True, text=True)
        print("✅ Pack completed successfully!")
        
        if result.stdout:
            print("📋 Pack output:")
            print(result.stdout)
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Pack failed with exit code {e.returncode}")
        if e.stdout:
            print("📋 Pack output:")
            print(e.stdout)
        if e.stderr:
            print("🚨 Pack errors:")
            print(e.stderr)
        return False
    
    # Create a README for the Windows build
    create_windows_readme(build_dir)
    
    # Create a simple run script
    create_run_script(build_dir)
    
    # Report build results
    report_build_results(build_dir)
    
    return True

def create_windows_readme(build_dir):
    """Create a README file for the Windows build directory."""
    readme_content = """# FleTodo - Windows Application

This directory contains the built Windows application version of FleTodo.

## What's included

- `FleTodo.exe` - Main executable file (if using single-file build)
- `FleTodo/` - Application folder containing all files (if using one-folder build)
- `run_flettodo.bat` - Convenient batch script to run the application
- `README.md` - This documentation

## Running the Application

### Method 1: Direct Execution
- If you see `FleTodo.exe`, double-click it to run the application
- If you see a `FleTodo/` folder, navigate into it and run `FleTodo.exe`

### Method 2: Using the Batch Script
- Double-click `run_flettodo.bat` to start the application

## Features

- ✅ Add new todo items
- ✅ Mark todos as complete/incomplete
- ✅ Delete unwanted todos
- ✅ Data persistence (saves automatically)
- ✅ Clean, modern interface
- ✅ No internet connection required

## System Requirements

- Windows 10 or later (64-bit)
- No additional software installation required
- All dependencies are included in the build

## Troubleshooting

### Application won't start
- Make sure you're running on Windows 10 or later
- Try running as administrator if you encounter permission issues
- Check Windows Defender or antivirus - they might flag the executable

### Data not saving
- Ensure the application has write permissions in its directory
- Check if the application folder is read-only

### Performance issues
- Close other resource-intensive applications
- Restart the application if it becomes unresponsive

## Technical Details

This Windows build was created using:
- Flet framework for Python
- PyInstaller for executable packaging
- All Python dependencies bundled

The application creates a local web server and opens the interface in a webview window,
providing a native app experience while using web technologies.

## Support

For issues or questions, please refer to the main FleTodo repository.

---

**🎉 Enjoy using FleTodo on Windows!**
"""
    
    readme_path = build_dir / "README.md"
    readme_path.write_text(readme_content, encoding='utf-8')
    print(f"📚 Created README.md")

def create_run_script(build_dir):
    """Create a batch script to run the application."""
    
    # Check what files exist to determine the correct run command
    exe_files = list(build_dir.glob("*.exe"))
    flettodo_dir = build_dir / "FleTodo"
    main_exe_win = flettodo_dir / "FleTodo.exe"  # Windows executable
    main_exe_unix = flettodo_dir / "FleTodo"     # Unix executable (for testing)
    
    if flettodo_dir.exists() and (main_exe_win.exists() or main_exe_unix.exists()):
        # One-folder build (most common with --onedir)
        run_command = r'start "" "FleTodo\FleTodo.exe"'
        if main_exe_win.exists():
            print(f"   Found Windows one-folder build at: {main_exe_win}")
        else:
            print(f"   Found Unix one-folder build at: {main_exe_unix} (will be FleTodo.exe on Windows)")
    elif exe_files:
        # Single-file build or other exe in root
        exe_file = exe_files[0]
        run_command = f'start "" "{exe_file.name}"'
        print(f"   Found single-file build at: {exe_file}")
    else:
        # Fallback - try both possibilities
        run_command = '''if exist "FleTodo\\FleTodo.exe" (
    start "" "FleTodo\\FleTodo.exe"
) else if exist "FleTodo.exe" (
    start "" "FleTodo.exe"
) else (
    echo FleTodo executable not found. Please check the build output.
    echo Expected locations:
    echo   - FleTodo\\FleTodo.exe
    echo   - FleTodo.exe
    pause
)'''
        print("   No executable found, creating fallback script")
    
    batch_content = f"""@echo off
echo Starting FleTodo - Simple Todo List Application...
echo.

REM Change to the directory containing this script
cd /d "%~dp0"

REM Run the FleTodo application
{run_command}

REM If there was an error, pause to show it
if errorlevel 1 (
    echo.
    echo Error starting FleTodo. Please check the executable file.
    pause
)
"""
    
    batch_path = build_dir / "run_flettodo.bat"
    batch_path.write_text(batch_content, encoding='utf-8')
    print(f"📄 Created run_flettodo.bat")

def report_build_results(build_dir):
    """Report the build results and file structure."""
    print("\n🎉 Windows Build Complete!")
    print("=" * 50)
    
    print(f"\n📦 Build directory: {build_dir}")
    print(f"📊 Files generated:")
    
    file_count = 0
    total_size = 0
    
    for root, dirs, files in os.walk(build_dir):
        for file in files:
            file_path = Path(root) / file
            if file_path.exists():
                file_count += 1
                file_size = file_path.stat().st_size
                total_size += file_size
                
                # Show main files
                if file.endswith(('.exe', '.bat', '.md')) or file == 'FleTodo.exe':
                    size_mb = file_size / (1024*1024)
                    print(f"   📁 {file_path.relative_to(build_dir)} ({size_mb:.2f} MB)")
    
    print(f"\n📋 Summary:")
    print(f"   Total files: {file_count}")
    print(f"   Total size: {total_size / (1024*1024):.2f} MB")
    
    print(f"\n🚀 To run the application:")
    print(f"   1. Navigate to: {build_dir}")
    print(f"   2. Double-click 'run_flettodo.bat'")
    print(f"   3. Or run FleTodo.exe directly")

if __name__ == "__main__":
    success = create_windows_build()
    sys.exit(0 if success else 1)