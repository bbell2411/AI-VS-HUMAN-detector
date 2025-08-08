from sqlalchemy import create_engine, inspect
from app.database import Base
from app.models.prediction import PredictionRecord
from app.setup_dbs import setup_database
from app.config import settings
from app.database import engine

class TestDatabaseSetup:
    def test_table_creation(self):
        """Test that setup_database actually creates the predictions table."""
        setup_database()
        
        inspector=inspect(engine)
        table_names=inspector.get_table_names()
        assert "predictions" in table_names
        assert "model_info" in table_names
        
    def test_prediction_table_has_columns(self):
        """Test to see if predictions table has correct columns"""
        expected_columns = [
            'id', 'text_content', 'content_type', 'prediction_result',
            'confidence_score', 'processing_time_ms', 'text_length', 'created_at'
        ]
        
        inspector=inspect(engine)
        
        columns=inspector.get_columns("predictions")
        column_names = [col['name'] for col in columns]
        for expected_col in expected_columns:
            assert expected_col in column_names
            
    def test_model_info_table_has_columns(self):
        """Test to see if model_info table has correct columns"""
        expected_columns = [
            'id', 'name', 'version', 'status',
            'accuracy', 'features'
        ]
        
        inspector=inspect(engine)
        
        columns=inspector.get_columns("model_info")
        column_names = [col['name'] for col in columns]
        for expected_col in expected_columns:
            assert expected_col in column_names
    
    