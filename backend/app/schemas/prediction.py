from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class PredictionRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=10000)
    
class PredictionResponse(BaseModel):
    result: str  
    confidence: float
    processing_time_ms: float
    timestamp: datetime
    text_length: int