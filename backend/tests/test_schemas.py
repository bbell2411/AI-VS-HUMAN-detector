from app.schemas.prediction import PredictionRequest, PredictionResponse
from datetime import datetime

def test_prediction_request():
    """Test that we can create a prediction request."""
    request = PredictionRequest(text="Hello world")
    assert request.text == "Hello world"

def test_prediction_response():
    """Test that we can create a prediction response."""
    response = PredictionResponse(
        result="human_written",
        confidence=0.85,
        processing_time_ms=150.0,
        timestamp=datetime.now(),
        text_length=11
    )
    assert response.result == "human_written"
    assert response.confidence == 0.85