import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from src.utils.logger import logger
from src.utils.exception import CustomException

# Define paths
RAW_DATA_PATH = "data/raw/dataset.csv"
PROCESSED_DATA_PATH = "data/processed/cleaned_dataset.csv"
os.makedirs("data/processed", exist_ok=True)

def preprocess_data():
    """Load, clean, impute, encode, and scale dataset."""
    try:
        logger.info("Loading raw dataset...")
        df = pd.read_csv(RAW_DATA_PATH)
        
        logger.info("Separating features and target variable...")
        X = df.drop(columns=["charges"])
        y = df["charges"]
        
        logger.info("Defining preprocessing pipeline...")
        numeric_features = ["age", "bmi", "children"]
        categorical_features = ["sex", "smoker", "region"]
        
        num_transformer = Pipeline([
            ("imputer", SimpleImputer(strategy="mean")),
            ("scaler", StandardScaler())
        ])
        
        cat_transformer = Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown='ignore'))
        ])
        
        preprocessor = ColumnTransformer(
            transformers=[
                ("num", num_transformer, numeric_features),
                ("cat", cat_transformer, categorical_features)
            ]
        )
        
        logger.info("Applying transformations...")
        X_processed = preprocessor.fit_transform(X)
        
        logger.info("Saving processed dataset...")
        processed_df = pd.DataFrame(X_processed, columns=preprocessor.get_feature_names_out())
        processed_df["charges"] = y.values  # Add target column back
        processed_df.to_csv(PROCESSED_DATA_PATH, index=False)
        
        logger.info(f"Processed dataset saved at {PROCESSED_DATA_PATH} with shape {processed_df.shape}")
        return processed_df
    except Exception as e:
        raise CustomException("Error in data processing", sys)

if __name__ == "__main__":
    preprocess_data()
