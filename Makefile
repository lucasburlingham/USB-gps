all: install run

install:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt

run:
	@echo "Running..."
	@python3 main.py