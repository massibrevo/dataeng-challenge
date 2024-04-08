# Makefile

# Setup the python environment and install dependencies
setup:
    python3 -m venv .venv
    . .venv/bin/activate && \
    pip install -r requirements.txt

# Run the application
run:
    python3 app/main.py

# Run tests
test:
    python3 -m unittest discover -s tests

.PHONY: setup run test
