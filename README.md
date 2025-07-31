# AI vs Human Text Detection

A machine learning project that classifies text as AI-generated or human-written using various ML algorithms and feature engineering techniques.

## 🎯 Project Overview

This project explores the challenging task of detecting AI-generated text vs human-written content. Through systematic experimentation with multiple algorithms and preprocessing techniques, I achieved 60.2% accuracy using an SVM model with PCA dimensionality reduction.

## 📊 Results

- **Best Model**: Support Vector Machine (SVM) with PCA
- **Accuracy**: 60.2%
- **Key Finding**: Even state-of-the-art models struggle with this task, making 60% a respectable baseline (considering limited dataset)

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

### Installation
```bash
git clone [your-repo-url]
cd ai-text-detector
pip install -r requirements.txt
