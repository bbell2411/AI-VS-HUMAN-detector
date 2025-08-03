import time
import joblib  
import os
from datetime import datetime
from app.schemas.prediction import PredictionRequest, PredictionResponse, ContentType
import re
import textstat
import numpy as np
from scipy.sparse import hstack

class MLService:
    def __init__(self):
        print("Loading your trained model...")
        path = os.path.join(os.path.dirname(__file__), '..', '..','..', 'models')
        model_path = os.path.join(os.path.dirname(__file__), '..', '..','..', 'models', 'svm_pca_model.joblib')
        self.vectorizer = joblib.load(os.path.join(path,'vectorizer.joblib'))
        self.imputer = joblib.load(os.path.join(path,"imputer.joblib"))
        self.scaler =  joblib.load(os.path.join(path,'scaler.joblib'))
        self.pca =  joblib.load(os.path.join(path,'pca.joblib'))
        self.model = joblib.load(model_path)
        
        print("ALL Models loaded!")
        
    def _extract_features_from_text(self, text, content_type):

                words = text.split()
                sentences = re.split(r'[.!?]+', text)
            
                features = {
                'word_count': len(words),
                'character_count': len(text),
                'sentence_count': len([s for s in sentences if s.strip()]),
                'lexical_diversity': len(set(words)) / max(len(words), 1),  
                'avg_sentence_length': len(words) / max(len(sentences), 1),
                'avg_word_length': sum(len(word) for word in words) / max(len(words), 1),
                'punctuation_ratio': len(re.findall(r'[^\w\s]', text)) / max(len(text), 1),
                'flesch_reading_ease': textstat.flesch_reading_ease(text),
                'gunning_fog_index': textstat.gunning_fog(text),           
                'grammar_errors': 0,
                'passive_voice_ratio': 0,
                'predictability_score': 0,
                'burstiness': 0,
                'sentiment_score': 0.5,
            }
                
                numeric_features = np.array([[
                    features['word_count'],
                    features['character_count'], 
                    features['sentence_count'],
                    features['lexical_diversity'],
                    features['avg_sentence_length'],
                    features['avg_word_length'],
                    features['punctuation_ratio'],
                    features['flesch_reading_ease'],
                    features['gunning_fog_index'],
                    features['grammar_errors'],
                    features['passive_voice_ratio'],
                    features['predictability_score'],
                    features['burstiness'],
                    features['sentiment_score']
    ]])

                dummy_columns = [
                ContentType.ARTICLE.value,           
                ContentType.BLOG_POST.value,         
                ContentType.CREATIVE_WRITING.value,  
                ContentType.ESSAY.value,             
                ContentType.NEWS_ARTICLE.value,      
                ContentType.PRODUCT_REVIEW.value,    
                ContentType.SOCIAL_MEDIA.value      
                ]
                content_dummies = np.array([[1 if col == content_type else 0 for col in dummy_columns]])
                text_features = self.vectorizer.transform([text]) 
                X_combined = hstack([numeric_features, content_dummies, text_features])
                return X_combined
        
    async def predict_text_origin(self, request: PredictionRequest) -> PredictionResponse:
        start_time = time.time()
        X_combined = self._extract_features_from_text(request.text, request.content_type)    
        
        X_imputed=self.imputer.transform(X_combined)
        X_scaled=self.scaler.transform(X_imputed)
        X_pca=self.pca.transform(X_scaled)
        
        prediction = self.model.predict(X_pca) 
        raw_result = prediction[0]  
        
        if raw_result == 0:
            result = "human_written"
        elif raw_result == 1:
            result = "ai_generated"
        
        processing_time = (time.time() - start_time) * 1000
        
        return PredictionResponse(
            result=result, 
            confidence=0.85,   
            processing_time_ms=round(processing_time, 2),
            timestamp=datetime.now(),
            text_length=len(request.text)
        )
        