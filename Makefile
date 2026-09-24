.PHONY: install test lint run docker-build docker-run clean docs

install:
	pip install -e ".[dev]"

test:
	pytest

test-cov:
	pytest --cov=src --cov-report=html

lint:
	ruff check .
	black --check .
	mypy src tests

format:
	black .
	ruff check --fix .

run:
	uvicorn mahe.main:app --reload

docker-build:
	docker build -t mahe-v2:latest .

docker-run:
	docker-compose up -d

docker-stop:
	docker-compose down

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage htmlcov .mypy_cache .ruff_cache build dist *.egg-info

docs:
	@echo "Documentation is available in the docs/ directory."
