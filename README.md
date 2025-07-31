# AI vs Human Text Detection

A machine learning project that classifies text as AI-generated or human-written using various ML algorithms and feature engineering techniques.

## 🎯 Project Overview

This project explores the challenging task of detecting AI-generated text vs human-written content. Through systematic experimentation with multiple algorithms and preprocessing techniques, I achieved 60.2% accuracy using an SVM model with PCA dimensionality reduction.

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
python main.py

## 📁 Project Structure
ai-text-detector/
├── main.py                 # Main execution script
├── src/
│   ├── data_loader.py      # Data loading
│   ├── feature_engineering.py  # Feature extraction
│   ├── model_trainer.py    # Model training and evaluation
│   └── logger_config.py    # Logging configuration
├── data/                   # Dataset directory
├── models/                 # Saved models
└── requirements.txt        # Dependencies

## 🔍 Key Insights
- Challenge Complexity: AI text detection is inherently difficult, even for humans
- Feature Importance: Combination of linguistic and stylistic features proved most effective
- Model Selection: SVM with proper preprocessing outperformed ensemble methods
- Balanced Performance: Model achieved equal performance on both AI and human text

## 📈 Future Improvements
- Experiment with deep learning approaches (BERT, RoBERTa)
- Collect more diverse training data
- Implement ensemble methods

