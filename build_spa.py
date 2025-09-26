#!/usr/bin/env python3
"""
Build script for FleTodo Single Page Application (SPA)
Creates a deployable web version of the Flet todo app.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

def create_spa_build():
    """Create the SPA build using Flet's publish command."""
    
    # Get project directory
    project_dir = Path(__file__).parent
    release_dir = project_dir / "release"
    
    print("🚀 Building FleTodo SPA...")
    print(f"📁 Project directory: {project_dir}")
    print(f"📦 Release directory: {release_dir}")
    
    # Clean existing release directory
    if release_dir.exists():
        print("🧹 Cleaning existing release directory...")
        shutil.rmtree(release_dir)
    
    # Build command with optimized settings for SPA deployment
    build_cmd = [
        "flet", "publish",
        str(project_dir / "main.py"),
        "--distpath", str(release_dir),
        "--app-name", "FleTodo",
        "--app-short-name", "FleTodo", 
        "--app-description", "A simple and elegant todo list application built with Flet",
        "--web-renderer", "html",  # Use HTML renderer for better compatibility
        "--route-url-strategy", "hash",  # Use hash routing for SPA
        "--pwa-background-color", "#FFFFFF",
        "--pwa-theme-color", "#0175C2"
    ]
    
    print("⚙️  Running Flet build command...")
    print(f"   Command: {' '.join(build_cmd)}")
    
    try:
        result = subprocess.run(build_cmd, cwd=project_dir, check=True, capture_output=True, text=True)
        print("✅ Build completed successfully!")
        
        if result.stdout:
            print("📋 Build output:")
            print(result.stdout)
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed with exit code {e.returncode}")
        if e.stdout:
            print("📋 Build output:")
            print(e.stdout)
        if e.stderr:
            print("🚨 Build errors:")
            print(e.stderr)
        return False
    
    # Create a README for the release
    create_release_readme(release_dir)
    
    # Create a simple test server script
    create_test_server_script(release_dir)
    
    # Report build results
    report_build_results(release_dir)
    
    return True

def create_release_readme(release_dir):
    """Create a README file for the release directory."""
    readme_content = """# FleTodo - Single Page Application

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
"""
    
    readme_path = release_dir / "README.md"
    readme_path.write_text(readme_content)
    print(f"📄 Created release README: {readme_path}")

def create_test_server_script(release_dir):
    """Create a simple test server script for local testing."""
    server_script = """#!/usr/bin/env python3
\"\"\"
Simple HTTP server for testing FleTodo SPA locally.
Run this script and open http://localhost:8080 in your browser.
\"\"\"

import http.server
import socketserver
import webbrowser
import os

PORT = 8080

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add headers for CORS and security
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🚀 FleTodo test server starting...")
        print(f"🌐 Server running at: http://localhost:{PORT}")
        print(f"📱 Open the URL in your browser to test the app")
        print(f"⏹️  Press Ctrl+C to stop the server")
        print()
        
        # Try to open browser automatically
        try:
            webbrowser.open(f'http://localhost:{PORT}')
            print("🎯 Browser should open automatically")
        except:
            print("ℹ️  Please manually open http://localhost:8080 in your browser")
        
        print()
        httpd.serve_forever()
"""
    
    server_path = release_dir / "test_server.py"
    server_path.write_text(server_script)
    server_path.chmod(0o755)  # Make executable
    print(f"🖥️  Created test server script: {server_path}")

def report_build_results(release_dir):
    """Report the build results and file structure."""
    print("\n🎉 SPA Build Complete!")
    print("=" * 50)
    
    print(f"\n📦 Release directory: {release_dir}")
    print(f"📊 Total files generated:")
    
    file_count = 0
    total_size = 0
    
    for root, dirs, files in os.walk(release_dir):
        for file in files:
            file_path = Path(root) / file
            if file_path.exists():
                file_count += 1
                total_size += file_path.stat().st_size
    
    print(f"   Files: {file_count}")
    print(f"   Total size: {total_size / (1024*1024):.2f} MB")
    
    print(f"\n📋 Main files:")
    main_files = ["index.html", "manifest.json", "main.dart.js", "python.js"]
    for file in main_files:
        file_path = release_dir / file
        if file_path.exists():
            size = file_path.stat().st_size / 1024
            print(f"   ✅ {file} ({size:.1f} KB)")
        else:
            print(f"   ❌ {file} (missing)")
    
    print(f"\n🚀 Deployment Instructions:")
    print(f"   1. Upload the contents of '{release_dir}' to your web hosting")
    print(f"   2. Or run 'python3 {release_dir}/test_server.py' for local testing")
    print(f"   3. The app will be available as a fully functional SPA")
    
    print(f"\n✨ FleTodo SPA is ready for deployment!")

if __name__ == "__main__":
    success = create_spa_build()
    sys.exit(0 if success else 1)