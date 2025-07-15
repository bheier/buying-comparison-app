import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Buying Comparison App", layout="wide")
st.title("📊 Buying Comparison App")

# Input
tickers = st.text_input("Enter stock or ETF tickers (comma-separated):", value="AAPL, TSLA, MSFT")

if tickers:
    tickers = [t.strip().upper() for t in tickers.split(",")]
    st.subheader("📈 Real-Time Summary")

    results = []

    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info

            pe_ratio = info.get("trailingPE", None)
            price = info.get("regularMarketPrice", None)
            forward_pe = info.get("forwardPE", None)
            dividend_yield = info.get("dividendYield", 0)

            score = 0
            if pe_ratio and pe_ratio > 0:
                score += 1 / pe_ratio
            if forward_pe and forward_pe > 0:
                score += 1 / forward_pe
            score += dividend_yield or 0

            results.append({
                "Ticker": ticker,
                "Price": price,
                "P/E": pe_ratio,
                "Forward P/E": forward_pe,
                "Dividend Yield": dividend_yield,
                "Score": round(score, 4)
            })

        except Exception as e:
            st.warning(f"Could not load data for {ticker}: {e}")

    if results:
        df = pd.DataFrame(results).sort_values(by="Score", ascending=False)
        st.dataframe(df, use_container_width=True)
        st.success(f"🎯 Best Buy Today: {df.iloc[0]['Ticker']}")
