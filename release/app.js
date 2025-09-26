// FleTodo JavaScript Application

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
});