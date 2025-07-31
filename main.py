from src.data_loader import load_data
from src.feature_engineering import create_features
from src.model_trainer import train_and_eval

if __name__ == "__main__":
       
    DATA_PATH = 'data/ai_human_content_detection_dataset.csv'

    print("--- Starting AI Text Detection Pipeline ---")

df = load_data(DATA_PATH)

X_full,y=create_features(df)

train_and_eval(X_full, y)
print("\n--- Pipeline Finished ---")

