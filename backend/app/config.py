from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str
    
    # API
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "ML Text Detector"
    
    # ML Model
    MODEL_PATH: str = "./ml_models/trained_model.pkl"
    
    # Environment
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"

settings = Settings()