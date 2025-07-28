import pandas as pd

df = pd.read_csv('data/ai_human_content_detection_dataset.csv')
print(df.shape)         
print(df.columns)      
print(df.head(2))