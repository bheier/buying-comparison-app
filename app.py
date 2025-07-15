import streamlit as st
import yfinance as yf
import pandas as pd
from model.forecast import forecast_returns

st.set_page_config(page_title="Buying Comparison App", layout="wide")
st.title("📊 Buying Comparison App")

# Input section
tickers = st.text_input("Enter stock or ETF tickers (comma-separated):", value="AAPL, TSLA, MSFT")

if tickers:
    tickers = [t.strip().upper() for t in tickers.split(",")]
    st.subheader("📈 Real-Time Analysis")

    results = []

    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info

            pe_ratio = info.get("trailingPE", None)
            forward_pe = info.get("forwardPE", None)
            price = info.get("regularMarketPrice", None)
            dividend_yield = info.get("dividendYield", 0)

            # Forecast future returns
            returns = forecast_returns(ticker)
            expected_5yr = returns.get("5yr", 0)

            # Scoring: higher = better
            score = 0
            if pe_ratio and pe_ratio > 0:
                score += 1 / pe_ratio
            if forward_pe and forward_pe > 0:
                score += 1 / forward_pe
            score += dividend_yield or 0
            score += expected_5yr / 10  # weight 5yr CAGR (as percent)

            results.append({
                "Ticker": ticker,
                "Price": price,
                "P/E": pe_ratio,
                "Forward P/E": forward_pe,
                "Dividend Yield": round(dividend_yield * 100, 2) if dividend_yield else None,
                "5YR Forecasted Return (%)": expected_5yr,
                "Score": round(score, 4)
            })

        except Exception as e:
            st.warning(f"Could not load data for {ticker}: {e}")

    # Display results
    if results:
        df = pd.DataFrame(results).sort_values(by="Score", ascending=False)
        st.dataframe(df, use_container_width=True)
        st.success(f"🎯 Best Buy Today: {df.iloc[0]['Ticker']}")
