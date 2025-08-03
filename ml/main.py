import logging
from src.logger_config import setup_logger
from src.data_loader import load_data
from src.feature_engineering import create_features
from src.model_trainer import train_and_eval

if __name__ == "__main__":
       
    setup_logger()

    logger = logging.getLogger(__name__)
    
    DATA_PATH = 'data/ai_human_content_detection_dataset.csv'

    logger.info("--- Starting AI Text Detection Pipeline ---")

df = load_data(DATA_PATH)

X_full,y,vectorizer=create_features(df)

train_and_eval(X_full, y,vectorizer)
logger.info("\n--- Pipeline Finished ---")

