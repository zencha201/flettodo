#!/usr/bin/env python3
"""
Create a standalone HTML/CSS/JavaScript version of FleTodo
This version will work without external dependencies.
"""

import os  
import json
from pathlib import Path

def create_standalone_spa():
    """Create a standalone SPA version."""
    
    project_dir = Path(__file__).parent
    release_dir = project_dir / "docs"
    
    print("🚀 Creating standalone FleTodo SPA...")
    
    # Create release directory
    release_dir.mkdir(exist_ok=True)
    
    # Create the main HTML file
    create_html_file(release_dir)
    
    # Create CSS styles
    create_css_file(release_dir)
    
    # Create JavaScript functionality
    create_js_file(release_dir)
    
    # Create manifest for PWA
    create_manifest(release_dir)
    
    # Create icons (using data URIs for simplicity)
    create_icons(release_dir)
    
    # Create documentation
    create_docs(release_dir)
    
    # Create .nojekyll for GitHub Pages
    nojekyll_path = release_dir / ".nojekyll"
    nojekyll_path.touch()
    print(f"📄 Created .nojekyll for GitHub Pages")
    
    print("✅ Standalone SPA created successfully!")
    print(f"📁 Location: {release_dir}")
    print("🌐 Open index.html in a web browser to test")

def create_html_file(release_dir):
    """Create the main HTML file."""
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FleTodo - Simple Todo List</title>
    
    <!-- PWA Manifest -->
    <link rel="manifest" href="manifest.json">
    
    <!-- Favicon -->
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E📝%3C/text%3E%3C/svg%3E">
    
    <!-- Apple Touch Icon -->
    <link rel="apple-touch-icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E📝%3C/text%3E%3C/svg%3E">
    
    <!-- Theme color -->
    <meta name="theme-color" content="#0175C2">
    
    <!-- CSS -->
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header class="app-header">
            <h1>📝 FleTodo</h1>
            <p class="subtitle">A simple and elegant todo list</p>
        </header>
        
        <main class="main-content">
            <!-- Add todo section -->
            <section class="add-todo-section">
                <div class="input-group">
                    <input 
                        type="text" 
                        id="todoInput" 
                        placeholder="Enter a new todo item..."
                        class="todo-input"
                        maxlength="200"
                    >
                    <button id="addBtn" class="add-btn">Add Todo</button>
                </div>
            </section>
            
            <hr class="divider">
            
            <!-- Todo list section -->
            <section class="todo-list-section">
                <h2>Your Todos:</h2>
                <div id="todoList" class="todo-list">
                    <div class="empty-state">
                        <p>No todos yet. Add one above!</p>
                    </div>
                </div>
            </section>
        </main>
        
        <footer class="app-footer">
            <p>Built with ❤️ using HTML, CSS & JavaScript</p>
            <p class="storage-info">Data is saved in your browser's local storage</p>
        </footer>
    </div>
    
    <!-- JavaScript -->
    <script src="app.js"></script>
</body>
</html>"""
    
    html_path = release_dir / "index.html"
    html_path.write_text(html_content)
    print(f"📄 Created index.html")

def create_css_file(release_dir):
    """Create the CSS styles file."""
    css_content = """/* FleTodo Styles */

/* Reset and base styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    line-height: 1.6;
    color: #333;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    padding: 20px;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    background: white;
    border-radius: 20px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    min-height: calc(100vh - 40px);
    display: flex;
    flex-direction: column;
}

/* Header */
.app-header {
    background: linear-gradient(135deg, #0175C2 0%, #0056b3 100%);
    color: white;
    padding: 30px 20px;
    text-align: center;
}

.app-header h1 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
    font-weight: 300;
}

.subtitle {
    font-size: 1.1rem;
    opacity: 0.9;
}

/* Main content */
.main-content {
    flex: 1;
    padding: 30px;
}

/* Add todo section */
.add-todo-section {
    margin-bottom: 30px;
}

.input-group {
    display: flex;
    gap: 15px;
    flex-wrap: wrap;
}

.todo-input {
    flex: 1;
    min-width: 250px;
    padding: 12px 16px;
    border: 2px solid #e0e0e0;
    border-radius: 8px;
    font-size: 16px;
    transition: border-color 0.3s ease;
}

.todo-input:focus {
    outline: none;
    border-color: #0175C2;
    box-shadow: 0 0 0 3px rgba(1, 117, 194, 0.1);
}

.add-btn {
    padding: 12px 24px;
    background: #0175C2;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.1s ease;
    min-width: 120px;
}

.add-btn:hover {
    background: #0056b3;
    transform: translateY(-1px);
}

.add-btn:active {
    transform: translateY(0);
}

.divider {
    border: none;
    height: 1px;
    background: #e0e0e0;
    margin: 20px 0;
}

/* Todo list section */
.todo-list-section h2 {
    color: #333;
    margin-bottom: 20px;
    font-size: 1.5rem;
    font-weight: 500;
}

.todo-list {
    display: flex;
    flex-direction: column;
    gap: 15px;
}

.empty-state {
    text-align: center;
    padding: 40px 20px;
    color: #999;
    font-style: italic;
}

/* Todo item */
.todo-item {
    display: flex;
    align-items: center;
    padding: 15px;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    background: white;
    transition: all 0.3s ease;
    animation: slideIn 0.3s ease;
}

.todo-item:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    transform: translateY(-1px);
}

.todo-item.completed {
    background: #f8f9fa;
    border-color: #d4edda;
}

.todo-checkbox {
    width: 20px;
    height: 20px;
    margin-right: 15px;
    cursor: pointer;
    accent-color: #0175C2;
}

.todo-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.todo-text {
    font-size: 16px;
    color: #333;
    transition: all 0.3s ease;
}

.todo-item.completed .todo-text {
    text-decoration: line-through;
    color: #999;
}

.todo-time {
    font-size: 12px;
    color: #999;
}

.delete-btn {
    background: none;
    border: none;
    color: #dc3545;
    font-size: 18px;
    cursor: pointer;
    padding: 8px;
    border-radius: 6px;
    transition: all 0.3s ease;
    opacity: 0.7;
}

.delete-btn:hover {
    background: rgba(220, 53, 69, 0.1);
    opacity: 1;
    transform: scale(1.1);
}

/* Footer */
.app-footer {
    background: #f8f9fa;
    padding: 20px;
    text-align: center;
    color: #666;
    font-size: 14px;
    border-top: 1px solid #e0e0e0;
}

.storage-info {
    margin-top: 5px;
    font-size: 12px;
    opacity: 0.8;
}

/* Animations */
@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(-10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideOut {
    from {
        opacity: 1;
        transform: translateX(0);
    }
    to {
        opacity: 0;
        transform: translateX(-100%);
    }
}

.todo-item.removing {
    animation: slideOut 0.3s ease forwards;
}

/* Responsive design */
@media (max-width: 600px) {
    body {
        padding: 10px;
    }
    
    .container {
        min-height: calc(100vh - 20px);
        border-radius: 15px;
    }
    
    .app-header {
        padding: 20px 15px;
    }
    
    .app-header h1 {
        font-size: 2rem;
    }
    
    .main-content {
        padding: 20px 15px;
    }
    
    .input-group {
        flex-direction: column;
    }
    
    .todo-input {
        min-width: unset;
    }
    
    .add-btn {
        min-width: unset;
    }
}

/* PWA specific styles */
@media (display-mode: standalone) {
    body {
        padding-top: 0;
    }
    
    .container {
        border-radius: 0;
        min-height: 100vh;
    }
}"""
    
    css_path = release_dir / "styles.css"
    css_path.write_text(css_content)
    print(f"🎨 Created styles.css")

def create_js_file(release_dir):
    """Create the JavaScript functionality file."""
    js_content = """// FleTodo JavaScript Application

class FleTodoApp {
    constructor() {
        this.todos = [];
        this.init();
    }
    
    init() {
        // Load existing todos from localStorage
        this.loadTodos();
        
        // Set up event listeners
        this.setupEventListeners();
        
        // Initial render
        this.renderTodoList();
        
        // Focus on input
        document.getElementById('todoInput').focus();
        
        console.log('🚀 FleTodo initialized successfully!');
    }
    
    setupEventListeners() {
        const todoInput = document.getElementById('todoInput');
        const addBtn = document.getElementById('addBtn');
        
        // Add todo button click
        addBtn.addEventListener('click', () => this.addTodo());
        
        // Enter key in input field
        todoInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.addTodo();
            }
        });
        
        // Clear input when focused for better UX
        todoInput.addEventListener('focus', () => {
            if (todoInput.value.trim() === '') {
                todoInput.select();
            }
        });
    }
    
    addTodo() {
        const todoInput = document.getElementById('todoInput');
        const text = todoInput.value.trim();
        
        if (!text) {
            // Shake animation for empty input
            todoInput.style.animation = 'shake 0.5s';
            setTimeout(() => todoInput.style.animation = '', 500);
            return;
        }
        
        const todo = {
            id: this.generateId(),
            text: text,
            completed: false,
            createdAt: new Date().toISOString()
        };
        
        this.todos.push(todo);
        todoInput.value = '';
        
        this.saveTodos();
        this.renderTodoList();
        
        // Focus back on input
        todoInput.focus();
        
        console.log('✅ Added todo:', todo.text);
    }
    
    toggleTodo(id) {
        const todo = this.todos.find(t => t.id === id);
        if (todo) {
            todo.completed = !todo.completed;
            this.saveTodos();
            this.renderTodoList();
            
            console.log(todo.completed ? '✅ Completed:' : '⭕ Uncompleted:', todo.text);
        }
    }
    
    deleteTodo(id) {
        const todoIndex = this.todos.findIndex(t => t.id === id);
        if (todoIndex !== -1) {
            const todo = this.todos[todoIndex];
            
            // Add removing animation
            const todoElement = document.querySelector(`[data-id="${id}"]`);
            if (todoElement) {
                todoElement.classList.add('removing');
                
                setTimeout(() => {
                    this.todos.splice(todoIndex, 1);
                    this.saveTodos();
                    this.renderTodoList();
                }, 300);
            }
            
            console.log('🗑️ Deleted todo:', todo.text);
        }
    }
    
    renderTodoList() {
        const todoList = document.getElementById('todoList');
        
        if (this.todos.length === 0) {
            todoList.innerHTML = `
                <div class="empty-state">
                    <p>No todos yet. Add one above!</p>
                </div>
            `;
            return;
        }
        
        // Sort todos: incomplete first, then by creation time
        const sortedTodos = [...this.todos].sort((a, b) => {
            if (a.completed !== b.completed) {
                return a.completed ? 1 : -1;
            }
            return new Date(a.createdAt) - new Date(b.createdAt);
        });
        
        todoList.innerHTML = sortedTodos.map(todo => `
            <div class="todo-item ${todo.completed ? 'completed' : ''}" data-id="${todo.id}">
                <input 
                    type="checkbox" 
                    class="todo-checkbox" 
                    ${todo.completed ? 'checked' : ''}
                    onchange="app.toggleTodo('${todo.id}')"
                >
                <div class="todo-content">
                    <div class="todo-text">${this.escapeHtml(todo.text)}</div>
                    <div class="todo-time">${this.formatDate(todo.createdAt)}</div>
                </div>
                <button 
                    class="delete-btn" 
                    onclick="app.deleteTodo('${todo.id}')"
                    title="Delete todo"
                >
                    🗑️
                </button>
            </div>
        `).join('');
        
        // Update document title with todo count
        const pendingCount = this.todos.filter(t => !t.completed).length;
        document.title = pendingCount > 0 ? `FleTodo (${pendingCount})` : 'FleTodo';
    }
    
    saveTodos() {
        try {
            localStorage.setItem('fleTodos', JSON.stringify(this.todos));
        } catch (error) {
            console.error('❌ Error saving todos:', error);
        }
    }
    
    loadTodos() {
        try {
            const saved = localStorage.getItem('fleTodos');
            if (saved) {
                this.todos = JSON.parse(saved);
                console.log(`📥 Loaded ${this.todos.length} todos from storage`);
            }
        } catch (error) {
            console.error('❌ Error loading todos:', error);
            this.todos = [];
        }
    }
    
    generateId() {
        return Date.now().toString(36) + Math.random().toString(36).substr(2);
    }
    
    escapeHtml(unsafe) {
        return unsafe
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }
    
    formatDate(isoString) {
        const date = new Date(isoString);
        const now = new Date();
        const diffMs = now - date;
        const diffHours = diffMs / (1000 * 60 * 60);
        const diffDays = diffMs / (1000 * 60 * 60 * 24);
        
        if (diffHours < 1) {
            return 'Just now';
        } else if (diffHours < 24) {
            return `${Math.floor(diffHours)} hour${Math.floor(diffHours) === 1 ? '' : 's'} ago`;
        } else if (diffDays < 7) {
            return `${Math.floor(diffDays)} day${Math.floor(diffDays) === 1 ? '' : 's'} ago`;
        } else {
            return date.toLocaleDateString();
        }
    }
}

// Add shake animation CSS dynamically
const shakeCSS = `
@keyframes shake {
    0%, 100% { transform: translateX(0); }
    10%, 30%, 50%, 70%, 90% { transform: translateX(-10px); }
    20%, 40%, 60%, 80% { transform: translateX(10px); }
}
`;

const style = document.createElement('style');
style.textContent = shakeCSS;
document.head.appendChild(style);

// Initialize the app when DOM is loaded
let app;
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        app = new FleTodoApp();
    });
} else {
    app = new FleTodoApp();
}

// Service Worker registration for PWA
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('sw.js')
            .then(registration => {
                console.log('✅ Service Worker registered:', registration);
            })
            .catch(error => {
                console.log('❌ Service Worker registration failed:', error);
            });
    });
}

// Prevent zooming on input focus on iOS
document.addEventListener('touchstart', () => {
    if (document.activeElement.tagName === 'INPUT') {
        document.querySelector('meta[name=viewport]').setAttribute('content', 
            'width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no');
        setTimeout(() => {
            document.querySelector('meta[name=viewport]').setAttribute('content', 
                'width=device-width, initial-scale=1');
        }, 500);
    }
});"""
    
    js_path = release_dir / "app.js"
    js_path.write_text(js_content)
    print(f"⚡ Created app.js")

def create_manifest(release_dir):
    """Create PWA manifest file."""
    manifest = {
        "name": "FleTodo - Simple Todo List",
        "short_name": "FleTodo",
        "description": "A simple and elegant todo list application",
        "start_url": "./",
        "display": "standalone",
        "background_color": "#FFFFFF",
        "theme_color": "#0175C2",
        "orientation": "portrait-primary",
        "icons": [
            {
                "src": "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E📝%3C/text%3E%3C/svg%3E",
                "sizes": "any",
                "type": "image/svg+xml"
            }
        ]
    }
    
    manifest_path = release_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2))
    print(f"📱 Created manifest.json")

def create_icons(release_dir):
    """Create a simple service worker for PWA."""
    sw_content = """// FleTodo Service Worker

const CACHE_NAME = 'fletodo-v1';
const urlsToCache = [
    './',
    './index.html',
    './styles.css',
    './app.js',
    './manifest.json'
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => cache.addAll(urlsToCache))
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                // Return cached version or fetch from network
                return response || fetch(event.request);
            })
    );
});"""
    
    sw_path = release_dir / "sw.js"
    sw_path.write_text(sw_content)
    print(f"⚙️ Created sw.js (Service Worker)")

def create_docs(release_dir):
    """Create documentation files."""
    readme_content = """# FleTodo - Standalone Single Page Application

A simple and elegant todo list application built with pure HTML, CSS, and JavaScript.

## Features

✅ **Add Todos**: Create new todo items with a simple text input  
✅ **Mark Complete**: Check off completed tasks  
✅ **Delete Todos**: Remove tasks you no longer need  
✅ **Persistent Storage**: Data is saved in browser's localStorage  
✅ **Responsive Design**: Works on desktop and mobile devices  
✅ **Progressive Web App**: Can be installed on devices  
✅ **Offline Support**: Works without internet connection  

## Quick Start

1. **Open the app**: Simply open `index.html` in any modern web browser
2. **Add a todo**: Type in the input field and click "Add Todo" or press Enter
3. **Mark complete**: Click the checkbox next to any todo item
4. **Delete**: Click the 🗑️ button to remove a todo
5. **Data persistence**: Your todos are automatically saved and will be there when you return

## Deployment Options

### Static Web Hosting
Upload all files to any static hosting service:
- GitHub Pages
- Netlify  
- Vercel
- Amazon S3 + CloudFront
- Any web server

### Local Testing
Use Python's built-in server:
```bash
python3 -m http.server 8080
```
Then open http://localhost:8080

### Web Server
Configure any web server (Apache, Nginx) to serve the files.

## File Structure

```
docs/
├── index.html          # Main application file
├── styles.css          # Application styles
├── app.js             # Application logic
├── manifest.json      # PWA manifest
├── sw.js             # Service worker for offline support
└── README.md         # This documentation
```

## Browser Compatibility

Works in all modern browsers including:
- Chrome (65+)
- Firefox (60+)
- Safari (12+)
- Edge (79+)

## Technical Details

- **No external dependencies**: Everything runs locally
- **LocalStorage**: Data persists between sessions
- **Service Worker**: Enables offline functionality
- **Responsive CSS**: Mobile-first design
- **Vanilla JavaScript**: No frameworks required
- **Progressive Enhancement**: Works with JavaScript disabled (basic functionality)

## Data Privacy

- All data is stored locally in your browser
- No data is sent to external servers
- No tracking or analytics
- Complete privacy and control over your todos

## Customization

You can easily customize the app by editing:
- `styles.css` - Change colors, fonts, layout
- `app.js` - Modify functionality or add features
- `index.html` - Update structure or content

## License

MIT License - Feel free to use, modify, and distribute.

---

Built with ❤️ using pure web technologies."""
    
    readme_path = release_dir / "README.md"
    readme_path.write_text(readme_content)
    print(f"📚 Created README.md")

if __name__ == "__main__":
    create_standalone_spa()