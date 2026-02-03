from src.data_loader import DataLoader
from src.visualization import Visualizer
from src.models import build_lstm_model, build_gru_model
from src.train import train_model
from src.forecast import Forecaster
import pandas as pd
import numpy as np
from src.config import SEQ_LENGTH

def main():
    print("=== COVID-19 Data Tracking and Forecasting ===")
    
    loader = DataLoader()
    confirmed, deaths, recovered = loader.load_data()
    
    ts_confirmed = loader.preprocess_data(confirmed)
    global_cases = loader.get_global_cases(ts_confirmed)
    
    viz = Visualizer()
    print("Generating EDA plots...")
    viz.plot_global_trend(global_cases, title="Global Confirmed Cases")
    viz.plot_daily_cases(global_cases, title="Global Daily New Cases")
    viz.plot_top_countries(ts_confirmed, top_n=10)
    
    print("Preparing data for training...")
    X, y, scaler = loader.prepare_training_data(global_cases)
    X_train, y_train, X_test, y_test = loader.split_data(X, y, split_ratio=0.8)
    
    print(f"Train Shape: {X_train.shape}, Test Shape: {X_test.shape}")
    
    print("\n--- Training LSTM Model ---")
    lstm = build_lstm_model((X_train.shape[1], 1))
    hist_lstm, trained_lstm = train_model(lstm, X_train, y_train, X_test, y_test, "lstm_model")
    
    forecaster_lstm = Forecaster(trained_lstm, scaler)
    y_true, y_pred_lstm, mae, rmse = forecaster_lstm.evaluate(X_test, y_test, "LSTM")
    viz.plot_predictions(y_true, y_pred_lstm, title="LSTM Predictions vs Actual")
    
    print("\n--- Forecasting Future ---")
    last_sequence = X_test[-1].reshape(1, SEQ_LENGTH, 1)
    future_cases = forecaster_lstm.predict_next_days(last_sequence, days=30)
    
    last_date = global_cases.index[-1]
    future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=30)
    
    viz.plot_forecast(global_cases.index, global_cases.values, future_dates, future_cases.flatten(), title="LSTM Future 30 Day Forecast")
    
    print("\n=== Pipeline Completed Successfully ===")
    print("Check /plots for visualizations.")
    print("Check /models for saved models.")

if __name__ == "__main__":
    main()
