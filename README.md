# AI vs Human Text Detection

A machine learning project that classifies text as AI-generated or human-written using various ML algorithms and feature engineering techniques.

## 🎯 Project Overview

This project explores the challenging task of detecting AI-generated text vs human-written content. Through systematic experimentation with multiple algorithms and preprocessing techniques, I achieved 60.2% accuracy using an SVM model with PCA dimensionality reduction.

## 📊 Dataset

This project uses the **AI vs Human Content Detection Dataset** from Kaggle, which contains labeled examples of AI-generated and human-written text across various content types.

- **Source**: [Kaggle - AI vs Human Content Detection](https://www.kaggle.com/datasets/pratyushpuri/ai-vs-human-content-detection-1000-record-in-2025)
- **Author**: Pratyush Puri
- **License**: Apache 2.0
- **Size**: 1,367 samples (estimated)
- **Features**: 17 columns including text content, linguistic metrics, readability scores
- **Labels**: Binary classification (AI vs Human)

*Dataset used under Apache 2.0 license terms for educational and research purposes.*

## 🛠️ Tech-stack
- Python 3.8+
- Scikit-learn: Machine learning algorithms and preprocessing
- Pandas: Data manipulation and analysis
- NumPy: Numerical computing
- SciPy: Sparse matrix operations


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
git clone [https://github.com/bbell2411/AI-VS-HUMAN-detector.git]
cd ai-text-detector
pip install -r requirements.txt
```

## Usage
```bash
python3 main.py
```
## 🔍 Key Insights
- Challenge Complexity: AI text detection is inherently difficult, even for humans
- Feature Importance: Combination of linguistic and stylistic features proved most effective
- Model Selection: SVM with proper preprocessing outperformed ensemble methods
- Balanced Performance: Model achieved equal performance on both AI and human text

## 📈 Future Improvements
- Experiment with deep learning approaches (BERT, RoBERTa)
- Collect more diverse training data
- Implement ensemble methods

