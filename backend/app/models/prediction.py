from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.sql import func
from app.database import Base

class PredictionRecord(Base):
    """Database table for storing prediction results."""
    __tablename__ = "predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    text_content = Column(Text, nullable=False)
    content_type = Column(String(50), nullable=False)
    prediction_result = Column(String(20), nullable=False)
    confidence_score = Column(Float, nullable=False)
    processing_time_ms = Column(Float, nullable=False)
    text_length = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())