import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack
 
 
def create_features(df):
     
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
    return X_full, y