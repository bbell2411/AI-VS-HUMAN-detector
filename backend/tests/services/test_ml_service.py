import pytest
from app.schemas.prediction import PredictionRequest, ContentType
from app.services.ml_service import MLService

@pytest.mark.asyncio
async def test_feature_extraction():
    """Test to see if features are extracted correctly"""
    ml_service=MLService()
    
    result=ml_service._extract_features_from_text("Hello world test", ContentType.ESSAY)
    
    assert result is not None
    assert result.shape[0] == 1 
    assert result.shape[1] > 0   
    print(f"Feature shape: {result.shape}")

@pytest.mark.asyncio
async def test_predict_with_real_model():
    """Test our prediction function."""
    ml_service = MLService() 
    
    request = PredictionRequest(text="This is a test sentence.", content_type=ContentType.ESSAY)
    
    result = await ml_service.predict_text_origin(request)
    
    assert result.result is not None 
    assert result.confidence > 0     
    assert result.text_length == 24
    assert result.timestamp is not None
    assert result.processing_time_ms > 0 
    print(f"Model predicted: {result.result}")
    
@pytest.mark.asyncio
async def test_different_content_types():
    """Test that different content types work."""
    ml_service = MLService()
    
    request = PredictionRequest(text="This is academic content.", content_type=ContentType.ACADEMIC_PAPER)
    result = await ml_service.predict_text_origin(request)
    
    assert result.result is not None
    print(f"Academic paper predicted: {result.result}")