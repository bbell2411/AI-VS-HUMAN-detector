import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack

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


