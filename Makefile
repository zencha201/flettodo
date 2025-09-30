.PHONY: help build validate serve clean test

help:
	@echo "FleTodo SPA Build Commands:"
	@echo ""
	@echo "  make build      - Build the standalone SPA"
	@echo "  make validate   - Validate the SPA build"
	@echo "  make serve      - Start local test server"
	@echo "  make clean      - Clean build artifacts"
	@echo "  make test       - Run tests"
	@echo "  make all        - Build and validate"
	@echo ""

build:
	@echo "🚀 Building FleTodo SPA..."
	python3 create_standalone_spa.py

validate:
	@echo "🔍 Validating SPA build..."
	python3 validate_spa.py

serve:
	@echo "🌐 Starting local server on http://localhost:8080"
	@echo "⏹️  Press Ctrl+C to stop"
	@cd docs && python3 test_server.py

clean:
	@echo "🧹 Cleaning build artifacts..."
	rm -rf docs/index.html docs/app.js docs/styles.css docs/manifest.json docs/sw.js

test:
	@echo "🧪 Running tests..."
	python3 test_todo.py

all: build validate
	@echo "✅ Build and validation complete!"
