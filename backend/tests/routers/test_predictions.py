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
    
    def test_text_too_long(self):
        """Test to see error display if text is too long"""
        payload={
            "text":"n"*10001,
            "content_type": "essay"
        }
        response = client.post(f"{settings.API_V1_STR}/predictions/", json=payload)
        assert response.status_code==422
        
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
        
    def test_model_info_get_request(self):
        """Test to check for correct response for model info get request"""
        response=client.get(f"{settings.API_V1_STR}/predictions/models/info")
        data=response.json()
        assert response.status_code==200
        assert "models" in data and "models" 
        assert "supported_content_types" in data 
        assert data["max_text_length"]==10000
        assert data["min_text_length"]==1
        
    def test_model_info_err_handling(self):
        """Test to display error for when model hasnt loaded or is unavailable"""
        from unittest.mock import patch
        with patch('app.routers.predictions.ml_service') as mock_ml_service:
            mock_ml_service.model = None 
            
            response=client.get(f"{settings.API_V1_STR}/predictions/models/info")
            data=response.json()
        assert response.status_code==503
        assert "Model not loaded" in data["detail"]