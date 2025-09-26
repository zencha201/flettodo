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
├── todo_app.py       # Main application with TodoApp class
├── main.py           # Entry point script
├── test_todo.py      # Test script for TodoItem functionality
├── requirements.txt  # Python dependencies
└── README.md         # This file
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
