def test_database_connection():
    """Test that we can connect to the database."""
    from app.database import engine
    from sqlalchemy import text
    
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        assert result.fetchone()[0] == 1
        
def test_prediction_record_creation():
    """Test creating a PredictionRecord object."""
    from app.models.prediction import PredictionRecord
    
    record = PredictionRecord(
        text_content="Test text",
        content_type="essay", 
        prediction_result="human_written",
        confidence_score=0.85,
        processing_time_ms=150.0,
        text_length=9
    )
    
    assert record.text_content == "Test text"
    assert record.prediction_result == "human_written"
    assert type(record.confidence_score)==float
    assert type(record.processing_time_ms)==float
    assert type(record.text_length)==int
    assert type(record.content_type)==str
    
    
    