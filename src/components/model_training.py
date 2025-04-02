import os
import joblib
import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from src.utils.logger import logger
from src.utils.exception import CustomException
import sys

# Define paths
TRAIN_DATA_PATH = "data/train/train.csv"
TEST_DATA_PATH = "data/test/test.csv"
MODEL_PATH = "models/xgb_regressor.pkl"
os.makedirs("models", exist_ok=True)

def train_model():
    """Train an XGBoost model and evaluate performance."""
    try:
        logger.info("Loading train and test datasets...")
        train_df = pd.read_csv(TRAIN_DATA_PATH)
        test_df = pd.read_csv(TEST_DATA_PATH)
        
        X_train = train_df.drop(columns=["charges"])
        y_train = train_df["charges"]
        X_test = test_df.drop(columns=["charges"])
        y_test = test_df["charges"]
        
        logger.info("Training XGBoost model...")
        model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        logger.info("Making predictions...")
        y_pred = model.predict(X_test)
        
        logger.info("Evaluating model performance...")
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = mse**0.5
        r2 = r2_score(y_test, y_pred)
        
        logger.info(f"MAE: {mae}")
        logger.info(f"MSE: {mse}")
        logger.info(f"RMSE: {rmse}")
        logger.info(f"R² Score: {r2}")
        
        logger.info("Saving trained model...")
        joblib.dump(model, MODEL_PATH)
        logger.info(f"Model saved at {MODEL_PATH}")
    except Exception as e:
        raise CustomException("Error in model training", sys)

if __name__ == "__main__":
    train_model()
