#!/usr/bin/env python3
"""
Simple HTTP server for testing FleTodo SPA locally.
Run this script and open http://localhost:8080 in your browser.
"""

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
