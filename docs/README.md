# FleTodo - Single Page Application

This directory contains the built Single Page Application (SPA) version of FleTodo.

## What's included

- `index.html` - Main application entry point
- `manifest.json` - PWA manifest for app metadata
- `assets/` - Application assets (fonts, images, etc.)
- `icons/` - Application icons for various sizes
- `*.js` files - JavaScript runtime and application code
- `app.tar.gz` - Packaged Python application source

## Deployment

To deploy this SPA:

1. **Static Web Hosting**: Upload all files to any static web hosting service (GitHub Pages, Netlify, Vercel, etc.)

2. **Local Testing**: Use the included `test_server.py` script:
   ```bash
   python3 test_server.py
   ```
   Then open http://localhost:8080 in your browser.

3. **Web Server**: Serve the files using any web server (Apache, Nginx, etc.)

## Features

✅ Add new todo items  
✅ Mark todos as completed  
✅ Delete todo items  
✅ Persistent storage using browser localStorage  
✅ Responsive design  
✅ Progressive Web App (PWA) support  

## Technical Details

- Built with Flet framework
- Uses HTML renderer for maximum compatibility  
- Hash-based routing for SPA behavior
- Pyodide for Python runtime in browser
- No external server dependencies after deployment

## Browser Compatibility

Works in all modern browsers that support:
- ES6 JavaScript
- Service Workers
- Local Storage
- WebAssembly (for Pyodide)
