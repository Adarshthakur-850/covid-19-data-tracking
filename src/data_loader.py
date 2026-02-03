import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from .config import CONFIRMED_URL, DEATHS_URL, RECOVERED_URL, SEQ_LENGTH

class DataLoader:
    def __init__(self):
        self.scaler = MinMaxScaler(feature_range=(0, 1))

    def load_data(self):
        print("Loading data from JHU...")
        confirmed_df = pd.read_csv(CONFIRMED_URL)
        deaths_df = pd.read_csv(DEATHS_URL)
        recovered_df = pd.read_csv(RECOVERED_URL)
        return confirmed_df, deaths_df, recovered_df

    def preprocess_data(self, df):
        df_grouped = df.groupby('Country/Region').sum(numeric_only=True)
        df_grouped = df_grouped.drop(columns=['Lat', 'Long'])
        df_ts = df_grouped.T
        df_ts.index = pd.to_datetime(df_ts.index)
        return df_ts

    def get_global_cases(self, df_ts):
        return df_ts.sum(axis=1)

    def prepare_training_data(self, series):
        data = series.values.reshape(-1, 1)
        scaled_data = self.scaler.fit_transform(data)
        
        X, y = [], []
        for i in range(SEQ_LENGTH, len(scaled_data)):
            X.append(scaled_data[i-SEQ_LENGTH:i, 0])
            y.append(scaled_data[i, 0])
            
        X, y = np.array(X), np.array(y)
        X = np.reshape(X, (X.shape[0], X.shape[1], 1))
        
        return X, y, self.scaler

    def split_data(self, X, y, split_ratio=0.8):
        train_size = int(len(X) * split_ratio)
        X_train, X_test = X[:train_size], X[train_size:]
        y_train, y_test = y[:train_size], y[train_size:]
        return X_train, y_train, X_test, y_test
