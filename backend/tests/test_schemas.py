from app.schemas.prediction import PredictionRequest, PredictionResponse, ContentType, ModelInfo
from datetime import datetime

def test_content_type_enum():
    """Test that ContentType enum works correctly."""
    
    expected_types = ["academic_paper", "article", "blog_post", "creative_writing", 
                     "essay", "news_article", "product_review", "social_media"]
    actual_types = [content_type.value for content_type in ContentType]

    assert ContentType.ACADEMIC_PAPER=="academic_paper"
    assert ContentType.ARTICLE=="article"
    assert ContentType.BLOG_POST=="blog_post"
    assert ContentType.CREATIVE_WRITING=="creative_writing"
    assert ContentType.ESSAY=="essay"
    assert ContentType.NEWS_ARTICLE=="news_article"
    assert ContentType.PRODUCT_REVIEW=="product_review"
    assert ContentType.SOCIAL_MEDIA=="social_media"
    assert set(actual_types) == set(expected_types)
    
def test_prediction_request():
    """Test that we can create a prediction request."""
    request = PredictionRequest(
        text="Hello world",
        content_type=ContentType.ACADEMIC_PAPER
        )
    assert request.text == "Hello world"
    assert request.content_type == ContentType.ACADEMIC_PAPER
    assert request.content_type.value == "academic_paper"

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
    
def test_model_info_request():
    """Test the model info schema"""
    model_info=ModelInfo(
        name="Test Model",
        version="1.0.0", 
        status="loaded",
        accuracy="85%",
        features=["TF-IDF", "linguistic"])
    assert model_info.name == "Test Model"
    assert model_info.version == "1.0.0"
    assert len(model_info.features) == 2
    
