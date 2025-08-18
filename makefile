.PHONY: help dev docker-build docker-run docker-dev deploy test install

help: ## help 
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

dev: ## Run development server locally
	cd backend && uvicorn app.main:app --reload --port 8000
install: ## Install dependencies
	cd backend && pip3 install -r requirements.txt

docker-build: ## Build Docker image
	docker build -f backend/Dockerfile -t ml-detector-api .

docker-run: ## Run Docker container
	docker run -p 8000:8000 --env-file backend/.env.production ml-detector-api

docker-dev: docker-build docker-run 

test: ## Run full backend tests
	cd backend && pytest --disable-warnings -v

clean: ## Clean up cache files
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name "*.pyc" -delete