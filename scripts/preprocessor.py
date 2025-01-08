import pandas as pd

def load_and_preprocess_data(file_path):
    # Load dataset
    data = pd.read_csv(file_path)
    
    # Mengisi nilai NaN dengan median
    data.fillna(data.median(numeric_only=True), inplace=True)
    
    return data
