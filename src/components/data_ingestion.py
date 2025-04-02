import os
import pandas as pd
import requests
import sys
from src.utils.logger import logger
from src.utils.exception import CustomException

# Define file paths
DATA_DIR = "data/raw"
os.makedirs(DATA_DIR, exist_ok=True)
FILE_PATH = os.path.join(DATA_DIR, "dataset.csv")

def download_data(url):
    """Downloads dataset from the given URL."""
    try:
        logger.info(f"Downloading data from {url}")
        response = requests.get(url)
        response.raise_for_status()
        
        with open(FILE_PATH, "wb") as file:
            file.write(response.content)
        
        logger.info(f"Dataset downloaded successfully at {FILE_PATH}")
    except Exception as e:
        raise CustomException("Failed to download dataset", sys)

def load_data():
    """Loads the dataset into a Pandas DataFrame."""
    try:
        logger.info("Loading dataset...")
        df = pd.read_csv(FILE_PATH)
        logger.info(f"Dataset loaded successfully with shape {df.shape}")
        return df
    except Exception as e:
        raise CustomException("Failed to load dataset", sys)

if __name__ == "__main__":
    dataset_url = "https://raw.githubusercontent.com/haissaoui/Portfolio-Project-US-Medical-Insurance-Costs/refs/heads/main/insurance.csv"
    download_data(dataset_url)
    df = load_data()
    print(df.head())
