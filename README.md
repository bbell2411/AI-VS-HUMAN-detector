# TextGuardApi

A machine learning-powered REST API that detects AI-generated text using advanced NLP techniques and FastAPI.

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue)](https://www.docker.com/)

## 🎯 Project Overview

TextGuardAPI is a production-ready REST API that provides real-time text classification services through a robust, scalable backend architecture. Built with FastAPI and deployed using modern DevOps practices, this project demonstrates full-stack engineering capabilities by integrating machine learning models into a high-performance web service.

The API processes text submissions through an optimized ML pipeline, stores predictions in a PostgreSQL database, and provides comprehensive analytics - all while maintaining sub-100ms response times. The entire system is containerized with Docker and deployed to cloud infrastructure with automated CI/CD.

## 🚀 Live Demo

**API Documentation**: [https://textguardapi-production.up.railway.app/docs](https://textguardapi-production.up.railway.app/docs)

## Key Achievements
- **Production-Ready API**: Fully documented RESTful endpoints with automatic OpenAPI/Swagger documentation
- **Scalable Architecture**: Asynchronous request handling supporting concurrent predictions
- **Cloud Deployment**: Containerized application deployed with automated pipelines and environment management
- **Comprehensive Testing**: Unit and integration tests ensuring reliability and maintainability
- **ML Integration**: Seamlessly integrated scikit-learn models with efficient preprocessing pipelines

## 📊 Dataset

This project uses the **AI vs Human Content Detection Dataset** from Kaggle, which contains labeled examples of AI-generated and human-written text across various content types.

- **Source**: [Kaggle - AI vs Human Content Detection](https://www.kaggle.com/datasets/pratyushpuri/ai-vs-human-content-detection-1000-record-in-2025)
- **Author**: Pratyush Puri
- **License**: Apache 2.0
- **Size**: 1,367 samples (estimated)
- **Features**: 17 columns including text content, linguistic metrics, readability scores
- **Labels**: Binary classification (AI vs Human)

*Dataset used under Apache 2.0 license terms for educational and research purposes.*

## 🛠️ Tech Stack

### Backend & API
- **FastAPI**: Modern async web framework with automatic API documentation
- **PostgreSQL/Supabase**: Cloud database for prediction storage and analytics
- **Docker**: Containerization for consistent deployments
- **Uvicorn**: Lightning-fast ASGI server
- **Pydantic**: Data validation and serialization
- **SQLAlchemy**: ORM for database operations
- **Python 3.11**: Latest Python for performance improvements
  
### Machine Learning
- **Scikit-learn**: Model training and preprocessing pipelines
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing and array operations
- **NLTK**: Text preprocessing and tokenization
- **Joblib**: Efficient model serialization
- **SciPy**: Sparse matrix operations for TF-IDF
  
### DevOps & Deployment
- **Docker**: Container orchestration
- **Railway/Render**: Cloud hosting platforms
- **GitHub Actions**: CI/CD pipeline
- **pytest**: Testing framework
- **Makefile**: Build automation

## 🔧 Technical Approach

### Feature Engineering
- **Text Features**: TF-IDF vectorization with n-grams (1-3)
- **Linguistic Features**: Word count, sentence length, readability scores
- **Style Features**: Punctuation ratio, passive voice, sentiment analysis

### Models Tested
- Random Forest
- Logistic Regression  
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)

### Preprocessing Pipeline
1. NAN value imputation
2. Feature scaling (StandardScaler)
3. Dimensionality reduction (PCA - 95% variance)

## 🚀 Getting Started

### Quick Start with Docker (Recommended)
```bash
# Clone the repository
git clone https://github.com/bbell2411/TextGuardApi.git
cd TextGuardApi


# Build and run with Docker (uses cloud database)
make docker-dev

# API available at http://localhost:8000/docs

# Running tests
make test

# Available Commands
make help
make docker-dev
make test
make clean
```
## 🔍 Engineering Insights
- **API Performance**: Achieved <100ms response time through model caching and async processing
- **Scalability**: Docker containerization enables horizontal scaling
- **Testing Strategy**: 85% code coverage with unit and integration tests
- **Model Serving**: Efficient model loading with singleton pattern

## 📈 Future Improvements
- Experiment with deep learning approaches (BERT, RoBERTa)
- Collect more diverse training data
- Implement ensemble methods
- Add Redis caching for frequent predictions
- implement API rate limiting and authentication
