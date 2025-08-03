from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class ContentType(str, Enum):
    ACADEMIC_PAPER="academic_paper"
    ARTICLE="article"
    BLOG_POST="blog_post"
    CREATIVE_WRITING="creative_writing"
    ESSAY = "essay"
    NEWS_ARTICLE="news_article"
    PRODUCT_REVIEW="product_review"
    SOCIAL_MEDIA="social_media"
    

class PredictionRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=10000)
    content_type: ContentType = Field(default=ContentType.ESSAY, description="Type of content")
    
class PredictionResponse(BaseModel):
    result: str  
    confidence: float
    processing_time_ms: float
    timestamp: datetime
    text_length: int