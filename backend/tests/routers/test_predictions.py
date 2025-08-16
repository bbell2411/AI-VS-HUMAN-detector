from fastapi.testclient import TestClient
from app.main import app
from app.config import settings
from app.database import SessionLocal
from app.models.prediction import PredictionRecord


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
        
    def test_get_all_predictions(self):
        """Test to ensure all predictions are being returned"""
        test_data = [
            {"text": "Test prediction 1", "content_type": "essay"},
            {"text": "Test prediction 2", "content_type": "article"},
            {"text": "Test prediction 3", "content_type": "blog_post"}
        ]
        for data in test_data:
            response=client.post(f"{settings.API_V1_STR}/predictions/",json=data)
            assert response.status_code==200
            
        
        response=client.get(f"{settings.API_V1_STR}/predictions/")
        data=response.json()
        assert response.status_code==200
        assert isinstance(data, list)
        assert len(data) >= 3
        
        if len(data) > 0:
            first_pred = data[0]
            required_fields = ["result", "confidence", "processing_time_ms", "timestamp", "text_length"]
            for field in required_fields:
                assert field in first_pred
             
    
    def test_get_all_data_returns_correct_result(self):
        """Tests get returns correct metadata"""
        
        payload = {
            "text": "Known test text for verification",
            "content_type": "essay"
        }
        
        post_res=client.post(f"{settings.API_V1_STR}/predictions/", json=payload)
        assert post_res.status_code==200
        post_data=post_res.json()
        
        get_res=client.get(f"{settings.API_V1_STR}/predictions/")
        assert get_res.status_code==200
        get_data=get_res.json()
        
        end_res=None
        
        for pred in get_data:
            if pred["text_length"] == len(payload["text"]):
                end_res=pred
                break
            
        assert end_res is not None
        assert end_res["confidence"]== post_data["confidence"]
        assert end_res["result"]== post_data["result"]
    
    def test_get_all_predictions_empty_database(self):
        """Test GET when non predictions exist"""
        
        response=client.get(f"{settings.API_V1_STR}/predictions/")
        assert response.status_code==200
        data= response.json()
        assert isinstance(data,list)
        assert len(data)==0
    def test_get_prediction_by_id(self):
        """Test to get prediction by it's ID"""
        payload = {
        "text": "Test text for ID retrieval",
        "content_type": "essay"
    }
        post_response=client.post(f"{settings.API_V1_STR}/predictions/",json=payload)
        assert post_response.status_code==200
                
        response = client.get(f"{settings.API_V1_STR}/predictions/1")
        assert response.status_code==200
        data = response.json()
        
        required_fields = ["result", "confidence", "processing_time_ms", "timestamp", "text_length"]
        for field in required_fields:
            assert field in data
            
        assert data["text_length"] == len(payload["text"])

    def test_get_prediction_by_id_bad_request(self):
        """Test for when id is not an integer (validation error)"""
        response= client.get(f"{settings.API_V1_STR}/predictions/notInt")
        assert response.status_code==422
        
    def test_get_prediction_by_id_not_found(self):
        """Test for when id does not exist in the database"""
        response=client.get(f"{settings.API_V1_STR}/predictions/298764")
        assert response.status_code==404
        
    def test_get_prediction_by_id_empty_list(self):
        """Test for when id exists and returns empty list instead of 404"""
        
    def test_get_prediction_by_id_negative_id(self):
        """Test for negative ID returns 400."""
        response = client.get(f"{settings.API_V1_STR}/predictions/-1")
        assert response.status_code == 400