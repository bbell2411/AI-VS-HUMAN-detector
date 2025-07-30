import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.impute import SimpleImputer

df = pd.read_csv('data/ai_human_content_detection_dataset.csv')

#all numeric features
X_numeric=df[['word_count', 'character_count',
       'sentence_count', 'lexical_diversity', 'avg_sentence_length',
       'avg_word_length', 'punctuation_ratio', 'flesch_reading_ease',
       'gunning_fog_index', 'grammar_errors', 'passive_voice_ratio',
       'predictability_score', 'burstiness', 'sentiment_score']]
#vectorise text content
vectorizer = TfidfVectorizer(max_features=100)  
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

#Original model withoit scaling and PCA
model=RandomForestClassifier(random_state=42)
model.fit(X_train_imputed, y_train)

#Evaluate original model
y_pred = model.predict(X_test_imputed)
print("First model eval: ",classification_report(y_test, y_pred))

#Scale trainig and test data
scaler = StandardScaler(with_mean=False)  # with_mean=False for sparse matrices
X_train_scaled = scaler.fit_transform(X_train_imputed) #fit and transform only on training data
X_test_scaled= scaler.transform(X_test_imputed)

#model with scaled sparse matrices
model_scaled=RandomForestClassifier(random_state=42)
model_scaled.fit(X_train_scaled, y_train)
#Evaluate model_scaled
y_pred1 = model_scaled.predict(X_test_scaled)
print("First model with scaling eval: ",classification_report(y_test, y_pred1))

#convert sparse matrices to dense
X_train_scaled_dense = X_train_scaled.toarray()  
X_test_scaled_dense = X_test_scaled.toarray()

#Apply PCA to capture 95% variance
pca=PCA(n_components=0.95)
X_train_pca = pca.fit_transform(X_train_scaled_dense)
X_test_pca = pca.transform(X_test_scaled_dense)

#2nd Classifier model with scaled and PCA transformed data
model2=RandomForestClassifier(random_state=42)
model2.fit(X_train_pca, y_train)

#Evaluate model2
y_pred2 = model2.predict(X_test_pca)
print("Second model eval (scaling and pca): ",classification_report(y_test, y_pred2))


#improve model accuracy
