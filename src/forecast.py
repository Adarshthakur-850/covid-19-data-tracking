import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
from .config import SEQ_LENGTH, PREDICT_DAYS

class Forecaster:
    def __init__(self, model, scaler):
        self.model = model
        self.scaler = scaler

    def predict_next_days(self, last_sequence, days=PREDICT_DAYS):
        curr_seq = last_sequence.copy()
        predictions = []

        for _ in range(days):
            pred = self.model.predict(curr_seq, verbose=0)
            predictions.append(pred[0, 0])
            
            new_val = pred.reshape(1, 1, 1)
            curr_seq = np.append(curr_seq[:, 1:, :], new_val, axis=1)
            
        return self.scaler.inverse_transform(np.array(predictions).reshape(-1, 1))

    def evaluate(self, X_test, y_test, model_name="Model"):
        predictions = self.model.predict(X_test)
        
        y_test_inv = self.scaler.inverse_transform(y_test.reshape(-1, 1))
        pred_inv = self.scaler.inverse_transform(predictions)
        
        mae = mean_absolute_error(y_test_inv, pred_inv)
        rmse = np.sqrt(mean_squared_error(y_test_inv, pred_inv))
        
        print(f"--- {model_name} Evaluation ---")
        print(f"MAE: {mae:.4f}")
        print(f"RMSE: {rmse:.4f}")
        
        return y_test_inv, pred_inv, mae, rmse
