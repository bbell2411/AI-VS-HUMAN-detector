import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.config import settings
client=TestClient(app)

class TestPredictionsRouter:
    
    def test_predict_text_origin_success(self):
        """Test successful prediction via HTTP POST"""

        payload = {
            "text": "im a human",
            "content_type": "essay"
        }
        response = client.post(f"{settings.API_V1_STR}/predictions/", json=payload)
        data = response.json()
        print(data)
        assert "result" in data
        assert "timestamp" in data
        assert "processing_time_ms" in data
        assert data["result"] in ["human_written", "ai_generated", "uncertain"]
        assert data["confidence"] > 0
        assert data["text_length"] == len(payload["text"])
    
    def test_text_too_short(self):
        """Test to see error display if text is too short"""
        payload={
            "text":"no",
            "content_type": "essay"
        }
        response = client.post(f"{settings.API_V1_STR}/predictions/", json=payload)
        assert response.status_code==400
        assert response.json()["detail"]== "Text must be at least 10 characters long"
    
    def test_if_value_is_valid(self):
        """Test to see error display if content types in post request is valid"""
        payload={
            "text":"yes i was unable to move! it hurt!",
            "content_type": "random"
        }
        response = client.post(f"{settings.API_V1_STR}/predictions/", json=payload)
        assert response.status_code==422
    def test_if_missing_keys(self):
        """Test to see error display for when missing keys"""
        payload={
            "content_type": "essay"
        }
        response = client.post(f"{settings.API_V1_STR}/predictions/", json=payload)
        assert response.status_code==422
