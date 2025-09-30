#!/usr/bin/env python3
"""
Validate the SPA build to ensure all required files are present and correct.
"""

import sys
from pathlib import Path
import json

def validate_spa_build():
    """Validate that the SPA build is complete and correct."""
    
    project_dir = Path(__file__).parent
    docs_dir = project_dir / "docs"
    
    print("🔍 Validating FleTodo SPA build...")
    print(f"📁 Checking directory: {docs_dir}")
    print()
    
    errors = []
    warnings = []
    
    # Check if docs directory exists
    if not docs_dir.exists():
        errors.append("docs/ directory does not exist")
        print("❌ FAILED: docs/ directory not found")
        return False
    
    # Required files
    required_files = {
        "index.html": "Main HTML file",
        "app.js": "Application JavaScript",
        "styles.css": "Application styles",
        "manifest.json": "PWA manifest",
        "sw.js": "Service worker",
        "README.md": "Documentation",
        ".nojekyll": "GitHub Pages config"
    }
    
    print("✅ Required files:")
    for filename, description in required_files.items():
        filepath = docs_dir / filename
        if filepath.exists():
            size = filepath.stat().st_size
            print(f"   ✓ {filename:20s} ({size:>6,} bytes) - {description}")
        else:
            errors.append(f"Missing required file: {filename}")
            print(f"   ✗ {filename:20s} - {description} - MISSING")
    
    print()
    
    # Validate HTML structure
    print("🔍 Validating HTML structure...")
    index_path = docs_dir / "index.html"
    if index_path.exists():
        html_content = index_path.read_text()
        checks = [
            ("<!DOCTYPE html>", "DOCTYPE declaration"),
            ('<meta name="viewport"', "Viewport meta tag"),
            ('manifest.json', "PWA manifest link"),
            ('styles.css', "CSS stylesheet link"),
            ('app.js', "JavaScript file"),
            ('<div id="todoList"', "Todo list container"),
            ('<input', "Input field"),
        ]
        
        for check, desc in checks:
            if check in html_content:
                print(f"   ✓ {desc}")
            else:
                warnings.append(f"HTML missing: {desc}")
                print(f"   ⚠ {desc} - NOT FOUND")
    
    print()
    
    # Validate manifest.json
    print("🔍 Validating manifest.json...")
    manifest_path = docs_dir / "manifest.json"
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text())
            required_keys = ["name", "short_name", "start_url", "display", "icons"]
            for key in required_keys:
                if key in manifest:
                    print(f"   ✓ {key}: {manifest[key] if key != 'icons' else f'{len(manifest[key])} icon(s)'}")
                else:
                    warnings.append(f"Manifest missing key: {key}")
                    print(f"   ⚠ {key} - MISSING")
        except json.JSONDecodeError as e:
            errors.append(f"manifest.json is not valid JSON: {e}")
            print(f"   ✗ Invalid JSON: {e}")
    
    print()
    
    # Validate JavaScript
    print("🔍 Validating JavaScript...")
    js_path = docs_dir / "app.js"
    if js_path.exists():
        js_content = js_path.read_text()
        js_checks = [
            ("localStorage", "LocalStorage usage"),
            ("addEventListener", "Event listeners"),
            ("getElementById", "DOM manipulation"),
            ("JSON.parse", "JSON parsing"),
            ("JSON.stringify", "JSON serialization"),
        ]
        
        for check, desc in js_checks:
            if check in js_content:
                print(f"   ✓ {desc}")
            else:
                warnings.append(f"JavaScript might be missing: {desc}")
                print(f"   ⚠ {desc} - NOT FOUND")
    
    print()
    
    # Summary
    print("=" * 60)
    if errors:
        print(f"❌ VALIDATION FAILED with {len(errors)} error(s):")
        for error in errors:
            print(f"   • {error}")
    elif warnings:
        print(f"⚠️  VALIDATION PASSED with {len(warnings)} warning(s):")
        for warning in warnings:
            print(f"   • {warning}")
        print("\n✅ Build is valid but could be improved")
        return True
    else:
        print("✅ VALIDATION PASSED - All checks successful!")
        print("\n🎉 FleTodo SPA build is ready for deployment!")
        return True
    
    if errors:
        return False
    
    return True

if __name__ == "__main__":
    success = validate_spa_build()
    sys.exit(0 if success else 1)
