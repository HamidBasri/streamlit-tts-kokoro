# TTS-Kokoro Project Commands

# Default recipe - show available commands
default:
    @just --list

# Install dependencies
install:
    uv sync

# Sync dependencies
sync:
    uv sync

# Activate environment
activate:
    source .venv/bin/activate

# Run the home application
run:
    python homepage.py

# Run Streamlit app in development mode
dev:
    streamlit run homepage.py

# Format code with black
format:
    black .

# Lint code with ruff
lint:
    ruff check .

# Fix linting issues automatically
lint-fix:
    ruff check --fix .

# Run all checks (format, lint)
check: format lint

# Run tests
test:
    pytest

# Clean up build artifacts
clean:
    rm -rf build/
    rm -rf dist/
    rm -rf *.egg-info/
    rm -rf .pytest_cache/
    rm -rf .coverage
    rm -rf htmlcov/
    find . -type d -name __pycache__ -exec rm -rf {} +
    find . -type f -name "*.pyc" -delete

# Update dependencies
update-deps:
    uv sync --upgrade
