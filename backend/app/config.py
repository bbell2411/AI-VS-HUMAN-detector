from pydantic_settings import BaseSettings
from typing import Optional
import os
import sys

class Settings(BaseSettings):
    DATABASE_URL: str = (
        "postgresql://postgres@localhost:5432/ml_detector_test" 
        if "pytest" in sys.modules or "PYTEST_CURRENT_TEST" in os.environ
        else "postgresql://postgres@localhost:5432/ml_detector"
    )
    
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "ML Text Detector"
    
    MODEL_PATH: str = "./ml_models/trained_model.pkl"
    
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
class Config:
        env_file = ".env"

settings = Settings()