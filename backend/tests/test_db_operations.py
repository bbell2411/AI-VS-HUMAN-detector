import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.main import app
from app.database import get_db
from app.config import settings
from app.models.prediction import PredictionRecord

client=TestClient(app)

class TestDbOperations:
    def test_prediction_saves_to_db(self):
        """Test that prediction saves to database"""
        payload = {
            "text": "This is a test text for database insertion.",
            "content_type": "essay"
        }
        response= client.post(f"{settings.API_V1_STR}/predictions/", json=payload)
        data= response.json()
        assert response.status_code==200
        assert data["result"] in ["human_written", "ai_generated"]
        
        with SessionLocal() as db:
            saved_record = db.query(PredictionRecord).filter(
                PredictionRecord.text_content == payload["text"]
            ).first()
            
        assert saved_record is not None
        assert saved_record.content_type=="essay"
        assert saved_record.prediction_result==data["result"]
        assert saved_record.confidence_score==data["confidence"]
        assert saved_record.text_length==len(payload["text"])
    
    def test_db_contains_predictions_after_api_call(self):
        texts = [
            "First test text for prediction.",
            "Second test text with different content.",
            "Third test text to verify database storage."
        ]
        
        for text in texts:
            payload={
                "text":text, 
                "content_type":"article"
            }
            response = client.post(f"{settings.API_V1_STR}/predictions/", json=payload)
            assert response.status_code==200
            
        with SessionLocal() as db:
            all_records = db.query(PredictionRecord).all()
            
        assert len(all_records) >= 3
            
        saved_texts = [record.text_content for record in all_records]
            
        for text in texts:
            assert text in saved_texts
            