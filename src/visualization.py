import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import os
from .config import PLOTS_DIR

class Visualizer:
    def __init__(self):
        sns.set(style="whitegrid")

    def save_plot(self, fig, filename):
        path = os.path.join(PLOTS_DIR, filename)
        if isinstance(fig, plt.Figure):
            fig.savefig(path)
            plt.close(fig)
        else:
            fig.write_image(path)
        print(f"Saved plot: {path}")

    def plot_global_trend(self, df_global, title="Global COVID-19 Cases"):
        plt.figure(figsize=(12, 6))
        plt.plot(df_global.index, df_global.values, label='Cumulative Cases')
        plt.title(title)
        plt.xlabel('Date')
        plt.ylabel('Cases')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        self.save_plot(plt.gcf(), f"{title.lower().replace(' ', '_')}.png")

    def plot_daily_cases(self, df_global, title="Global Daily New Cases"):
        daily_cases = df_global.diff().fillna(0)
        plt.figure(figsize=(12, 6))
        plt.bar(daily_cases.index, daily_cases.values, color='orange', label='Daily Cases')
        plt.title(title)
        plt.xlabel('Date')
        plt.ylabel('New Cases')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        self.save_plot(plt.gcf(), f"{title.lower().replace(' ', '_')}.png")

    def plot_top_countries(self, df, top_n=10, title="Top Countries by Cases"):
        last_date = df.index[-1]
        top_countries = df.loc[last_date].sort_values(ascending=False).head(top_n)
        
        plt.figure(figsize=(12, 6))
        sns.barplot(x=top_countries.values, y=top_countries.index, palette="viridis")
        plt.title(f"{title} (as of {last_date.date()})")
        plt.xlabel('Cases')
        plt.ylabel('Country')
        plt.tight_layout()
        self.save_plot(plt.gcf(), f"{title.lower().replace(' ', '_')}.png")

    def plot_predictions(self, y_test, y_pred, title="Model Predictions vs Actual"):
        plt.figure(figsize=(12, 6))
        plt.plot(y_test, label='Actual')
        plt.plot(y_pred, label='Predicted')
        plt.title(title)
        plt.xlabel('Time Step')
        plt.ylabel('Normalized Cases')
        plt.legend()
        self.save_plot(plt.gcf(), f"{title.lower().replace(' ', '_')}.png")
        
    def plot_forecast(self, historical_dates, historical_values, future_dates, future_values, title="Forecast"):
        plt.figure(figsize=(14, 7))
        plt.plot(historical_dates, historical_values, label='Historical')
        plt.plot(future_dates, future_values, label='Forecast', linestyle='--')
        plt.title(title)
        plt.xlabel('Date')
        plt.ylabel('Cases')
        plt.legend()
        plt.grid(True)
        self.save_plot(plt.gcf(), f"{title.lower().replace(' ', '_')}.png")
