.PHONY: test test-watch test-quiet dev install clean

# Run tests with clean output
test:
	PYTHONPATH=. pytest -v --asyncio-mode=auto --disable-warnings

# Run tests quietly (just pass/fail)
test-quiet:
	PYTHONPATH=. pytest -q --asyncio-mode=auto --disable-warnings

# Run tests and watch for changes
test-watch:
	PYTHONPATH=. pytest -v --maxfail=1 -x --asyncio-mode=auto --disable-warnings

# Start development server
dev:
	uvicorn app.main:app --reload --port 8000

# Install dependencies
install:
	pip install -r requirements.txt

# Clean cache files
clean:
	find . -type d -name "__pycache__" -delete
	find . -name "*.pyc" -delete