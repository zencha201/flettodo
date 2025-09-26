#!/usr/bin/env python3
"""
Flet Todo List Application

A single-page application (SPA) for managing todo items with the following features:
- Add new todo items
- Mark todos as completed  
- Delete todo items
- Data persistence using browser localStorage
- Dynamic UI updates
"""

import flet as ft
import json
from datetime import datetime
from typing import List, Dict, Any


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
        
        # Main container
        main_container = ft.Container(
            content=ft.Column([
                ft.Text("Todo List", size=24, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                input_row,
                ft.Divider(),
                ft.Text("Your Todos:", size=18, weight=ft.FontWeight.W_500),
                self.todo_list
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


def main(page: ft.Page):
    """Main application entry point."""
    TodoApp(page)


if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)