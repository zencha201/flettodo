#!/usr/bin/env python3
"""
Flet Todo List Application

A single-page application (SPA) for managing todo items with the following features:
- Add new todo items
- Mark todos as completed  
- Delete todo items
- Data persistence using browser localStorage
- Dynamic UI updates
- Export/Import todos to/from JSON files
"""

import flet as ft
import json
from datetime import datetime
from typing import List, Dict, Any
import os


class TodoItem:
    """Represents a single todo item with name, creation time, and completion status."""
    
    def __init__(self, name: str, creation_time: str = None, completed: bool = False, todo_id: str = None):
        self.name = name
        self.creation_time = creation_time or datetime.now().isoformat()
        self.completed = completed
        self.id = todo_id or str(hash(f"{name}_{self.creation_time}"))
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert todo item to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "creation_time": self.creation_time,
            "completed": self.completed
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TodoItem':
        """Create todo item from dictionary."""
        return cls(
            name=data["name"],
            creation_time=data["creation_time"],
            completed=data["completed"],
            todo_id=data["id"]
        )


class TodoApp:
    """Main Todo List Application."""
    
    def __init__(self, page: ft.Page):
        self.page = page
        self.todos: List[TodoItem] = []
        
        # Configure page
        self.page.title = "Flet Todo List"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.padding = 20
        
        # UI components
        self.todo_input = ft.TextField(
            hint_text="Enter a new todo item...",
            expand=True,
            on_submit=self.add_todo
        )
        
        self.add_button = ft.ElevatedButton(
            text="Add Todo",
            on_click=self.add_todo
        )
        
        self.todo_list = ft.Column(
            spacing=10,
            scroll=ft.ScrollMode.AUTO
        )
        
        # Status message text
        self.status_message = ft.Text(
            value="",
            size=14,
            color=ft.colors.GREEN_700,
            text_align=ft.TextAlign.CENTER
        )
        
        # FilePicker for import/export
        self.file_picker = ft.FilePicker(
            on_result=self.file_picker_result
        )
        self.page.overlay.append(self.file_picker)
        
        # Track current file operation
        self.current_operation = None
        
        # Load existing todos from localStorage
        self.load_todos()
        
        # Build and display UI
        self.build_ui()
    
    def build_ui(self):
        """Build the user interface."""
        # Top section: Input field and add button
        input_row = ft.Row(
            [self.todo_input, self.add_button],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        
        # Import/Export buttons at the bottom
        export_button = ft.ElevatedButton(
            text="📥 Export to JSON",
            icon=ft.icons.DOWNLOAD,
            on_click=self.export_todos_dialog,
            tooltip="Export todos to a JSON file"
        )
        
        import_button = ft.ElevatedButton(
            text="📤 Import from JSON",
            icon=ft.icons.UPLOAD,
            on_click=self.import_todos_dialog,
            tooltip="Import todos from a JSON file"
        )
        
        button_row = ft.Row(
            [export_button, import_button],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )
        
        # Main container
        main_container = ft.Container(
            content=ft.Column([
                ft.Text("Todo List", size=24, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                input_row,
                ft.Divider(),
                ft.Text("Your Todos:", size=18, weight=ft.FontWeight.W_500),
                self.todo_list,
                ft.Divider(),
                button_row,
                self.status_message
            ]),
            padding=20
        )
        
        self.page.add(main_container)
        self.update_todo_list()
    
    def add_todo(self, e=None):
        """Add a new todo item."""
        text = self.todo_input.value.strip()
        if text:
            todo = TodoItem(name=text)
            self.todos.append(todo)
            self.todo_input.value = ""
            self.save_todos()
            self.update_todo_list()
            self.page.update()
    
    def toggle_todo_completed(self, todo_id: str):
        """Toggle the completion status of a todo item."""
        for todo in self.todos:
            if todo.id == todo_id:
                todo.completed = not todo.completed
                break
        self.save_todos()
        self.update_todo_list()
        self.page.update()
    
    def delete_todo(self, todo_id: str):
        """Delete a todo item."""
        self.todos = [todo for todo in self.todos if todo.id != todo_id]
        self.save_todos()
        self.update_todo_list()
        self.page.update()
    
    def create_todo_row(self, todo: TodoItem) -> ft.Row:
        """Create a UI row for a todo item."""
        # Format creation time for display
        try:
            dt = datetime.fromisoformat(todo.creation_time)
            time_str = dt.strftime("%m/%d/%Y %H:%M")
        except:
            time_str = "Unknown"
        
        # Create checkbox for completion status
        checkbox = ft.Checkbox(
            value=todo.completed,
            on_change=lambda e: self.toggle_todo_completed(todo.id)
        )
        
        # Create todo text with strikethrough if completed
        todo_text = ft.Text(
            todo.name,
            size=16,
            color=ft.colors.GREY_600 if todo.completed else ft.colors.BLACK,
            style=ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH) if todo.completed else None
        )
        
        # Create time text
        time_text = ft.Text(
            time_str,
            size=12,
            color=ft.colors.GREY_500
        )
        
        # Create delete button
        delete_button = ft.IconButton(
            icon=ft.icons.DELETE,
            icon_color=ft.colors.RED_400,
            on_click=lambda e: self.delete_todo(todo.id),
            tooltip="Delete todo"
        )
        
        # Create the row layout
        return ft.Container(
            content=ft.Row([
                checkbox,
                ft.Column([
                    todo_text,
                    time_text
                ], spacing=2),
                delete_button
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=10,
            border=ft.border.all(1, ft.colors.GREY_300),
            border_radius=8,
            bgcolor=ft.colors.GREY_50 if todo.completed else ft.colors.WHITE
        )
    
    def update_todo_list(self):
        """Update the todo list display."""
        self.todo_list.controls.clear()
        
        if not self.todos:
            self.todo_list.controls.append(
                ft.Text(
                    "No todos yet. Add one above!",
                    size=16,
                    color=ft.colors.GREY_500,
                    italic=True
                )
            )
        else:
            # Sort todos: incomplete first, then by creation time
            sorted_todos = sorted(
                self.todos,
                key=lambda x: (x.completed, x.creation_time)
            )
            
            for todo in sorted_todos:
                self.todo_list.controls.append(self.create_todo_row(todo))
    
    def save_todos(self):
        """Save todos to localStorage."""
        try:
            todos_data = [todo.to_dict() for todo in self.todos]
            self.page.client_storage.set("todos", json.dumps(todos_data))
        except Exception as e:
            print(f"Error saving todos: {e}")
    
    def load_todos(self):
        """Load todos from localStorage."""
        try:
            todos_json = self.page.client_storage.get("todos")
            if todos_json:
                todos_data = json.loads(todos_json)
                self.todos = [TodoItem.from_dict(data) for data in todos_data]
        except Exception as e:
            print(f"Error loading todos: {e}")
            self.todos = []
    
    def export_todos_dialog(self, e=None):
        """Open file picker dialog to export todos to JSON."""
        self.current_operation = "export"
        self.file_picker.save_file(
            dialog_title="Export Todos to JSON",
            file_name="todos.json",
            allowed_extensions=["json"],
            file_type=ft.FilePickerFileType.CUSTOM
        )
    
    def import_todos_dialog(self, e=None):
        """Open file picker dialog to import todos from JSON."""
        self.current_operation = "import"
        self.file_picker.pick_files(
            dialog_title="Import Todos from JSON",
            allowed_extensions=["json"],
            file_type=ft.FilePickerFileType.CUSTOM,
            allow_multiple=False
        )
    
    def file_picker_result(self, e: ft.FilePickerResultEvent):
        """Handle file picker result for both import and export."""
        if self.current_operation == "export":
            self.export_todos_to_file(e)
        elif self.current_operation == "import":
            self.import_todos_from_file(e)
        self.current_operation = None
    
    def export_todos_to_file(self, e: ft.FilePickerResultEvent):
        """Export todos to a JSON file."""
        try:
            if e.path:
                # Prepare todos data
                todos_data = [todo.to_dict() for todo in self.todos]
                json_content = json.dumps(todos_data, indent=2, ensure_ascii=False)
                
                # Write to file
                with open(e.path, 'w', encoding='utf-8') as f:
                    f.write(json_content)
                
                self.show_status_message(
                    f"✅ Exported {len(self.todos)} todos to {os.path.basename(e.path)}",
                    ft.colors.GREEN_700
                )
            else:
                self.show_status_message("Export cancelled", ft.colors.GREY_600)
        except Exception as ex:
            self.show_status_message(f"❌ Error exporting: {str(ex)}", ft.colors.RED_700)
    
    def import_todos_from_file(self, e: ft.FilePickerResultEvent):
        """Import todos from a JSON file."""
        try:
            if e.files and len(e.files) > 0:
                file_path = e.files[0].path
                
                # Read from file
                with open(file_path, 'r', encoding='utf-8') as f:
                    json_content = f.read()
                
                # Parse JSON
                todos_data = json.loads(json_content)
                
                # Validate data structure
                if not isinstance(todos_data, list):
                    raise ValueError("Invalid JSON format: expected a list of todos")
                
                # Import todos
                imported_todos = [TodoItem.from_dict(data) for data in todos_data]
                self.todos = imported_todos
                
                # Save to localStorage
                self.save_todos()
                
                # Update UI
                self.update_todo_list()
                self.page.update()
                
                self.show_status_message(
                    f"✅ Imported {len(imported_todos)} todos from {os.path.basename(file_path)}",
                    ft.colors.GREEN_700
                )
            else:
                self.show_status_message("Import cancelled", ft.colors.GREY_600)
        except json.JSONDecodeError as ex:
            self.show_status_message(f"❌ Invalid JSON file: {str(ex)}", ft.colors.RED_700)
        except Exception as ex:
            self.show_status_message(f"❌ Error importing: {str(ex)}", ft.colors.RED_700)
    
    def show_status_message(self, message: str, color=None):
        """Display a status message to the user."""
        if color is None:
            color = ft.colors.GREEN_700
        self.status_message.value = message
        self.status_message.color = color
        self.page.update()
        
        # Clear message after 5 seconds
        import threading
        def clear_message():
            import time
            time.sleep(5)
            self.status_message.value = ""
            self.page.update()
        
        thread = threading.Thread(target=clear_message, daemon=True)
        thread.start()


def main(page: ft.Page):
    """Main application entry point."""
    TodoApp(page)


if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)