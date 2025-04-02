import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.utils.logger import logger
from src.utils.exception import CustomException
from src.utils.common import load_yaml,create_folder

data=load_yaml()

# Define paths
PROCESSED_DATA_PATH=data['data_preprocessing']['processed_data_path']
TRAIN_DATA_PATH = data['data_splitting']['train_data_path']
TEST_DATA_PATH = data['data_splitting']['test_data_path']

# Create directories
create_folder("data/train")
create_folder("data/test")

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
