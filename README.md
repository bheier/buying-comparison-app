# buying-comparison-app
# 📊 Buying Comparison App – ML-Powered Stock & ETF Screener

This application filters a custom list of stock and ETF tickers and identifies the best one to buy *right now* based on valuation, momentum, and forecasted returns.

## 🔧 Tech Stack
- Frontend: React (Progressive Web App)
- Backend: Python (Streamlit or FastAPI)
- Machine Learning: Facebook Prophet, Scikit-learn
- Data APIs: Yahoo Finance, Finnhub, yFinance

## 🧠 AI Features
- Forecasts 1, 3, 5, and 10-year annualized returns using time series modeling
- Applies ML-based scoring to rank assets by upside potential
- Flags tickers trading below projected fair value

## 🚀 Key Features
- Input any list of tickers (stocks or ETFs)
- Automatically filters and ranks the best buy today
- View historical vs projected returns
- Analyze key metrics: P/E, P/B, Yield, Sharpe Ratio, Beta, Momentum

## 📱 PWA Highlights
- Mobile-friendly, installable app
- Works offline with cached data
- Fast performance with service workers

## 📦 Deployment
- Backend: Streamlit Cloud or FastAPI on Google Cloud / Render
- Frontend: Vercel, Firebase, or Netlify

## 🛠️ Setup
1. Clone the repository
2. Add a `.env` file with your API keys (see `.env.example`)
3. Run backend: `streamlit run app.py` or `uvicorn main:app`
4. Run frontend: `npm install && npm run dev`

## 📍 Example Use Case
> “I’m tracking AAPL, TSLA, VGT, and SMH — which one is the best buy today based on real-time valuation and 5-year projected upside?”


