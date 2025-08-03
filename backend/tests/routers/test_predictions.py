import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.config import settings
client=TestClient(app)

class TestPredictionsRouter:
    
    def test_predict_test_origin_success(self):
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
