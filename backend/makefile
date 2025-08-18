.PHONY: test test-watch test-quiet dev install clean

test:
	DATABASE_URL="postgresql://postgres@localhost:5432/ml_detector_test" pytest --disable-warnings -v

test-quiet:
	DATABASE_URL="postgresql://postgres@localhost:5432/ml_detector_test" pytest --disable-warnings -q
	
setup-dbs:
	DATABASE_URL="postgresql://postgres@localhost:5432/ml_detector" PYTHONPATH=. python -m app.setup_dbs 

setup-test-dbs:
	DATABASE_URL="postgresql://postgres@localhost:5432/ml_detector_test" PYTHONPATH=. python -m app.setup_dbs

test-db:
	DATABASE_URL="postgresql://postgres@localhost:5432/ml_detector_test" pytest tests/test_db_setup.py -v -s

# Start development server
dev:
	uvicorn app.main:app --reload --port 8000

setup-prod-db:
	set -a; . ./.env.production; set +a; python3 -m app.setup_dbs
# Install dependencies
install:
	pip3 install -r requirements.txt
	
docker-build:
	docker build -t ml-detector-api .

docker-run:
	docker run -p 8000:8000 ml-detector-api

# Clean cache files
clean:
	find . -type d -name "__pycache__" -delete
	find . -name "*.pyc" -delete
