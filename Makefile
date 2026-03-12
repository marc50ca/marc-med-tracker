.PHONY: help install test lint format validate validate-hacs clean release

help:
	@echo "Marc Med Tracker - Development Commands"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  install       Install development dependencies"
	@echo "  test          Run tests"
	@echo "  lint          Run linters (ruff, black check)"
	@echo "  format        Format code (black, isort)"
	@echo "  validate      Validate manifest and services"
	@echo "  validate-hacs Validate HACS compatibility"
	@echo "  clean         Remove build artifacts"
	@echo "  release       Create release archive"
	@echo "  help          Show this help message"

install:
	pip install --upgrade pip
	pip install homeassistant voluptuous pyyaml
	pip install black isort ruff pytest

test:
	pytest tests/

lint:
	@echo "Running ruff..."
	ruff check marc_med_tracker/
	@echo "Checking formatting with black..."
	black --check marc_med_tracker/
	@echo "Checking imports with isort..."
	isort --check-only marc_med_tracker/

format:
	@echo "Formatting with black..."
	black marc_med_tracker/
	@echo "Sorting imports with isort..."
	isort marc_med_tracker/

validate: validate-hacs
	@echo "Validating manifest.json..."
	python scripts/validate_manifest.py
	@echo "Validating services.yaml..."
	python scripts/validate_services.py
	@echo "Checking Python syntax..."
	python -m py_compile marc_med_tracker/*.py

validate-hacs:
	@echo "Validating HACS compatibility..."
	python scripts/validate_hacs.py

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf **/__pycache__
	rm -rf **/*.pyc
	find . -name ".DS_Store" -delete

release: clean validate
	@echo "Creating release archive..."
	zip -r marc-med-tracker.zip \
		marc_med_tracker/ \
		docs/ \
		examples/ \
		README.md \
		OVERVIEW.md \
		CHANGELOG.md \
		LICENSE \
		-x "*.DS_Store" "*__pycache__*" "*.pyc"
	@echo "Release archive created: marc-med-tracker.zip"
