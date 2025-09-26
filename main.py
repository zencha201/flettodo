#!/usr/bin/env python3
"""
Main entry point for the Flet Todo List Application.
"""

from todo_app import main
import flet as ft

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)