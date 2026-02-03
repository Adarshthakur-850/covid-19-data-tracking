<<<<<<< HEAD
# COVID-19 Data Tracking and Time-Series Forecasting

A production-quality system to track, analyze, visualize, and forecast COVID-19 cases using Deep Learning (LSTM) on the JHU time-series dataset.

## Project Structure
```
covid-19 data tracking/
├── models/             # Saved .h5 models
├── plots/              # Generated visualizations
├── src/
│   ├── config.py       # Configuration and constants
│   ├── data_loader.py  # Data fetching and preprocessing
│   ├── visualization.py# Plotting functions
│   ├── models.py       # LSTM/GRU architecture
│   ├── train.py        # Training loop
│   └── forecast.py     # Evaluation and prediction
├── main.py             # Entry point
├── requirements.txt    # Dependencies
└── README.md           # This file
```

## Features
- **Data Engineering**: Automatic fetching from JHU GitHub, preprocessing, and sequence generation.
- **EDA**: Global trends, daily new cases, country-wise comparisons.
- **Deep Learning**: LSTM model for time-series forecasting.
- **Visualization**: Clear plots for analysis and predictions.

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main pipeline:
```bash
python main.py
```

## Output
- **Plots**: Saved in `plots/` directory.
- **Model**: Saved in `models/` directory.
=======
# covid-19-data-tracking
ml project
>>>>>>> e8eeffac7e11a09041111b0188b1105e5bf6b72f
