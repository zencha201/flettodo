# FleTodo - Windows Application

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
