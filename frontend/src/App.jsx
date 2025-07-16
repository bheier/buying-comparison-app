import React, { useState } from "react";

function App() {
  const [tickers, setTickers] = useState("AAPL, TSLA, MSFT");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleCompare = async () => {
    setLoading(true);
    try {
      // Replace with your Streamlit deployment URL or future API route
      const response = await fetch("http://localhost:8501/?tickers=" + encodeURIComponent(tickers));
      const data = await response.text(); // Use .json() if using API instead of Streamlit
      setResult(data);
    } catch (error) {
      setResult("Failed to fetch data.");
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
      <h1>📊 Buying Comparison App</h1>
      <p>Enter stocks or ETFs to compare. The app will tell you the best buy today based on value, yield, and forecast.</p>

      <input
        type="text"
        value={tickers}
        onChange={(e) => setTickers(e.target.value)}
        placeholder="Enter tickers like AAPL, TSLA, VGT"
        style={{ width: "60%", padding: "0.5rem", marginTop: "1rem" }}
      />

      <div>
        <button onClick={handleCompare} style={{ marginTop: "1rem", padding: "0.5rem 1rem" }}>
          Compare
        </button>
      </div>

      {loading && <p>Loading...</p>}
      {result && (
        <div style={{ marginTop: "2rem" }}>
          <h3>Results</h3>
          <pre>{result}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
