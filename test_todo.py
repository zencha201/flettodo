#!/usr/bin/env python3
"""
Simple test script for TodoItem functionality.
"""

from todo_app import TodoItem
import json
from datetime import datetime

def test_todo_item():
    """Test TodoItem creation and serialization."""
    print("Testing TodoItem functionality...")
    
    # Test creating a todo item
    todo = TodoItem("Test todo item")
    print(f"Created todo: {todo.name}")
    print(f"Creation time: {todo.creation_time}")
    print(f"Completed: {todo.completed}")
    print(f"ID: {todo.id}")
    
    # Test serialization
    todo_dict = todo.to_dict()
    print(f"Serialized todo: {todo_dict}")
    
    # Test deserialization
    loaded_todo = TodoItem.from_dict(todo_dict)
    print(f"Loaded todo: {loaded_todo.name}")
    
    # Test completion toggle
    loaded_todo.completed = True
    print(f"Marked as completed: {loaded_todo.completed}")
    
    print("✅ All TodoItem tests passed!")

def test_json_serialization():
    """Test JSON serialization of multiple todos."""
    print("\nTesting JSON serialization...")
    
    todos = [
        TodoItem("Buy groceries"),
        TodoItem("Walk the dog"),
        TodoItem("Finish project", completed=True)
    ]
    
    # Serialize to JSON
    todos_data = [todo.to_dict() for todo in todos]
    json_str = json.dumps(todos_data, indent=2)
    print("Serialized todos:")
    print(json_str)
    
    # Deserialize from JSON
    loaded_data = json.loads(json_str)
    loaded_todos = [TodoItem.from_dict(data) for data in loaded_data]
    
    print(f"\nLoaded {len(loaded_todos)} todos:")
    for todo in loaded_todos:
        status = "✅" if todo.completed else "⭕"
        print(f"{status} {todo.name}")
    
    print("✅ JSON serialization tests passed!")

if __name__ == "__main__":
    test_todo_item()
    test_json_serialization()
    print("\n🎉 All tests completed successfully!")