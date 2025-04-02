import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.utils.logger import logger
from src.utils.exception import CustomException

# Define paths
PROCESSED_DATA_PATH = "data/processed/cleaned_dataset.csv"
TRAIN_DATA_PATH = "data/train/train.csv"
TEST_DATA_PATH = "data/test/test.csv"

# Create directories
os.makedirs("data/train", exist_ok=True)
os.makedirs("data/test", exist_ok=True)

def split_data():
    """Load processed data, split into train and test sets, and save."""
    try:
        logger.info("Loading processed dataset...")
        df = pd.read_csv(PROCESSED_DATA_PATH)
        
        logger.info("Splitting dataset into train and test sets...")
        train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
        
        logger.info("Saving train and test datasets...")
        train_df.to_csv(TRAIN_DATA_PATH, index=False)
        test_df.to_csv(TEST_DATA_PATH, index=False)
        
        logger.info(f"Train dataset saved at {TRAIN_DATA_PATH} with shape {train_df.shape}")
        logger.info(f"Test dataset saved at {TEST_DATA_PATH} with shape {test_df.shape}")
    except Exception as e:
        raise CustomException("Error in data splitting", sys)

if __name__ == "__main__":
    split_data()
