#!/usr/bin/env python3
"""
Simple runner script for the FleTodo application.
This is the most convenient way to start the todo app.
"""

import sys
import os

# Add current directory to path so we can import our modules
sys.path.insert(0, os.path.dirname(__file__))

try:
    import flet as ft
    from todo_app import main
    
    print("🚀 Starting FleTodo - Flet Todo List Application...")
    print("💡 This will open in your web browser")
    print("📝 Features: Add todos, mark complete, delete, persistent storage")
    print("🔗 The app will be available at a local web address")
    print("")
    
    # Run the application
    ft.app(target=main, view=ft.WEB_BROWSER)
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("")
    print("🔧 To fix this, install the required dependencies:")
    print("   pip install -r requirements.txt")
    print("")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error starting application: {e}")
    sys.exit(1)