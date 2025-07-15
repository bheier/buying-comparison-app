from prophet import Prophet
import yfinance as yf
import pandas as pd
import numpy as np

def download_price_data(ticker, period="10y"):
    data = yf.download(ticker, period=period)
    df = data[["Close"]].reset_index()
    df.rename(columns={"Date": "ds", "Close": "y"}, inplace=True)
    return df

def forecast_returns(ticker):
    df = download_price_data(ticker)
    if len(df) < 100:
        return {}

    model = Prophet(daily_seasonality=False, yearly_seasonality=True)
    model.fit(df)

    future = model.make_future_dataframe(periods=365 * 10)  # Forecast 10 years
    forecast = model.predict(future)

    # Extract year-end forecasts
    forecast["year"] = forecast["ds"].dt.year
    yearly = forecast.groupby("year")["yhat"].last().reset_index()
    base_price = df["y"].iloc[-1]

    returns = {}
    for year in [1, 3, 5, 10]:
        target_year = pd.Timestamp.today().year + year
        future_price = yearly.loc[yearly["year"] == target_year, "yhat"].values
        if future_price.size > 0:
            cagr = (future_price[0] / base_price) ** (1 / year) - 1
            returns[f"{year}yr"] = round(cagr * 100, 2)  # % annualized return

    return returns
