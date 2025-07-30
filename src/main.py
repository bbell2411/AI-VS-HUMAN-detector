import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


df = pd.read_csv('data/ai_human_content_detection_dataset.csv')

results={}

highest_score={
       'model': None,
       'score': 0
}

models = {
    'RandomForest': RandomForestClassifier(random_state=42),
    'LogisticRegression': LogisticRegression(random_state=42, max_iter=100000),
    'SVM': SVC(random_state=42),
    'KNN': KNeighborsClassifier()
}


#all numeric features
X_numeric=df[['word_count', 'character_count',
       'sentence_count', 'lexical_diversity', 'avg_sentence_length',
       'avg_word_length', 'punctuation_ratio', 'flesch_reading_ease',
       'gunning_fog_index', 'grammar_errors', 'passive_voice_ratio',
       'predictability_score', 'burstiness', 'sentiment_score']]
#vectorise text content
vectorizer = TfidfVectorizer(
    max_features=950,  
    ngram_range=(1, 3), 
    min_df=2,  
    max_df=0.9,  
    sublinear_tf=True, 
    use_idf=True,
    smooth_idf=True
    )  
X_text = vectorizer.fit_transform(df['text_content'])  
#encode cat features to numeric
X_cat = pd.get_dummies(df['content_type'], drop_first=True)
#combine all features into a single matrix (np.hstack for dense arrays, hstack for sparse matrices)
X_non_text = np.hstack([X_numeric.values, X_cat.values])
X_full = hstack([X_non_text, X_text])

y=df['label']

#splitting dataset into train and test before scaling
X_train, X_test, y_train, y_test = train_test_split(
       X_full,
       y,
       test_size=0.2,
       random_state=42,
       stratify=y
)

#Impute nan/missing values
imputer = SimpleImputer(strategy='mean')
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)

#Train and evaluate all models (no scaling or PCA)
for name, model in models.items():
    model.fit(X_train_imputed, y_train)
    y_pred = model.predict(X_test_imputed)
    accuracy = accuracy_score(y_test, y_pred)
    results[name] = accuracy
    print(f"RAW MODEL EVAL: {name}: {accuracy:.3f}")
best_model = max(results, key=results.get)
if results[best_model] > highest_score["score"]:
       highest_score["score"] = results[best_model]
       highest_score["model"] = best_model
print("")
print(f"Best RAW Model: {best_model} with accuracy: {results[best_model]:.3f}")
print("---------------------------------------------")


#Scale trainig and test data
scaler = StandardScaler(with_mean=False)  
X_train_scaled = scaler.fit_transform(X_train_imputed) 
X_test_scaled= scaler.transform(X_test_imputed)


#convert sparse matrices to dense
X_train_scaled_dense = X_train_scaled.toarray()  
X_test_scaled_dense = X_test_scaled.toarray()

#Train and evaluate all models with scaled data
for name, model in models.items():
    model.fit(X_train_scaled_dense, y_train)
    y_pred = model.predict(X_test_scaled_dense)
    accuracy = accuracy_score(y_test, y_pred)
    results[name] = accuracy
    print(f"SCALED MODEL EVAL (DENSE): {name}: {accuracy:.3f}")
best_model = max(results, key=results.get)
if results[best_model] > highest_score["score"]:
       highest_score["score"] = results[best_model]
       highest_score["model"] = best_model
print("")
print(f"Best SCALED Model: {best_model} with accuracy: {results[best_model]:.3f}")
    
print("---------------------------------------------")

#Apply PCA to capture 95% variance
pca=PCA(n_components=0.95)
X_train_pca = pca.fit_transform(X_train_scaled_dense)
X_test_pca = pca.transform(X_test_scaled_dense)

#Train and evaluate all models with scaled + PCA data
for name, model in models.items():
    model.fit(X_train_pca, y_train)
    y_pred = model.predict(X_test_pca)
    accuracy = accuracy_score(y_test, y_pred)
    results[name] = accuracy
    print(f"PCA APPLIED MODEL EVAL {name}: {accuracy:.3f}")
if results[best_model] > highest_score["score"]:
       highest_score["score"] = results[best_model]
       highest_score["model"] = best_model
best_model = max(results, key=results.get)
print("")
print(f"Best PCA Model: {best_model} with accuracy: {results[best_model]:.3f}")
print("")
print("----------------------------------OVERALL RESULTS-----------------------------------")
print("")
print(f"BEST SCORING MODEL: {highest_score['model']} with accuracy: {highest_score['score']:.3f}")

print("-----------------------------------")

print(f"-----Optimising {highest_score['model']}-----")
