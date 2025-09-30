# FleTodo - Flet Todo List Application

A modern, single-page todo list application built with Python and Flet framework. Features a clean interface with persistent data storage using browser localStorage.

## Features

- ✅ **Add Todo Items**: Easy text input to create new tasks
- ✅ **Mark as Complete**: Check/uncheck todos to track completion
- ✅ **Delete Todos**: Remove unwanted items with a single click
- ✅ **Persistent Storage**: Data saved to browser localStorage
- ✅ **Dynamic Updates**: Real-time UI updates without page refresh
- ✅ **Responsive Design**: Clean, modern interface
- ✅ **Time Tracking**: Shows creation time for each todo

## Requirements

- Python 3.7+
- Flet framework

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/zencha201/flettodo.git
   cd flettodo
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

To start the todo application:

```bash
python todo_app.py
```

Or using the main entry point:

```bash
python main.py
```

The application will open in your default web browser.

## Building

### Web SPA Build

The project includes **two** build options for creating a web SPA:

#### Option 1: Standalone HTML/CSS/JS (Recommended)

Creates a pure HTML/CSS/JavaScript version with no external dependencies:

```bash
python create_standalone_spa.py
```

This creates a lightweight, standalone SPA in the `docs/` directory with:
- Pure HTML/CSS/JavaScript (no Python runtime needed)
- ~15KB total size (excluding icons)
- Works offline with service worker
- PWA support
- Perfect for GitHub Pages

#### Option 2: Flet-Based Build

Creates a full Flet web build using Python runtime in the browser:

```bash
python build_spa.py
```

This creates a complete Flet web version with Pyodide runtime (requires Flet installation).

**Note:** The standalone version is automatically built and deployed via GitHub Actions on every push to main.

### Windows Desktop Build

To create a Windows desktop executable:

```bash
python build_windows.py
```

This creates a Windows application in the `bin/win/` directory with:
- Standalone executable that doesn't require Python installation
- Convenient batch script for easy launching
- Complete documentation and usage instructions

**Requirements for Windows builds:**
- Python 3.7+
- Flet framework (`flet>=0.21.0`)
- PyInstaller (`pyinstaller>=6.0.0`)

The Windows build uses PyInstaller to create a self-contained executable that includes all dependencies.

### Using the Todo List

1. **Adding Todos**: Type your task in the input field and click "Add Todo" or press Enter
2. **Completing Todos**: Click the checkbox next to any todo to mark it as complete
3. **Deleting Todos**: Click the red delete button (🗑️) to remove a todo
4. **Viewing Todos**: All todos are displayed with creation time and completion status

### Data Persistence

Your todos are automatically saved to your browser's localStorage and will persist between sessions. No server or database required!

## Project Structure

```
flettodo/
├── todo_app.py           # Main application with TodoApp class
├── main.py               # Entry point script
├── test_todo.py          # Test script for TodoItem functionality
├── build_spa.py          # Build script for web SPA deployment
├── build_windows.py      # Build script for Windows desktop app
├── create_standalone_spa.py  # Standalone HTML/CSS/JS version
├── requirements.txt      # Python dependencies
├── bin/                  # Build output directory
│   └── win/             # Windows build artifacts
├── docs/                # SPA build artifacts
└── README.md            # This file
```

## Technical Details

### TodoItem Class

Each todo item contains:
- **name**: The todo text
- **creation_time**: ISO format timestamp
- **completed**: Boolean completion status  
- **id**: Unique identifier for the todo

### Storage Format

Todos are stored as JSON in browser localStorage:
```json
[
  {
    "id": "unique-id",
    "name": "Example todo",
    "creation_time": "2025-09-26T09:21:21.939687",
    "completed": false
  }
]
```

## Testing

Run the test suite to verify functionality:

```bash
python test_todo.py
```

## License

MIT License - see LICENSE file for details.

## GitHub Pages

This project is hosted on GitHub Pages and automatically deployed via GitHub Actions.

- **Live Site**: [https://zencha201.github.io/flettodo/](https://zencha201.github.io/flettodo/)
- **Auto-deploy**: Triggered on every push to `main` branch
- **Build Process**: Uses `create_standalone_spa.py` to generate static files
- **Deployment**: Files are deployed to `gh-pages` branch

### Manual Deployment

To manually deploy to GitHub Pages:

1. Build the SPA:
   ```bash
   python create_standalone_spa.py
   ```

2. The `docs/` directory is ready for deployment to any static hosting service

### CI/CD Pipeline

The repository includes a GitHub Actions workflow (`.github/workflows/build-spa.yml`) that:
- Automatically builds the SPA on every push
- Runs verification checks
- Deploys to GitHub Pages (on main branch)
- Stores build artifacts for 30 days