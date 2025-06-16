# 📊 Monte Carlo Simulation for Value at Risk (VaR) with Jump Diffusion Model

This project simulates future stock price paths using a Monte Carlo method with a **Geometric Brownian Motion + Jump Diffusion** model. It calculates **Value at Risk (VaR)** and **Conditional VaR (CVaR)**, identifies historical jumps in log returns, and outputs detailed simulation data and risk metrics in both graphical and CSV format.

---

## 🔧 Features

- ✅ Fetches historical stock data using `yfinance`
- ✅ Computes log-adjusted returns and statistical parameters
- ✅ Simulates multiple price paths using:
  - Geometric Brownian Motion
  - Poisson-driven Jump Diffusion
- ✅ Calculates:
  - Value at Risk (VaR)
  - Conditional VaR (CVaR / Expected Shortfall)
- ✅ Detects price jumps based on standard deviation cutoff
- ✅ Visualizes:
  - Simulated price paths
  - Histogram of final simulated prices with VaR overlay
- ✅ Saves:
  - Price path simulations
  - Jump event logs
  - Summary statistics
  - 
---

## 📁 Project Structure

markdown
Copy
Edit
# 📊 Monte Carlo Simulation for Value at Risk (VaR) with Jump Diffusion Model

This project simulates future stock price paths using a Monte Carlo method with a **Geometric Brownian Motion + Jump Diffusion** model. It calculates **Value at Risk (VaR)** and **Conditional VaR (CVaR)**, identifies historical jumps in log returns, and outputs detailed simulation data and risk metrics in both graphical and CSV format.

---

## 🔧 Features

- ✅ Fetches historical stock data using `yfinance`
- ✅ Computes log-adjusted returns and statistical parameters
- ✅ Simulates multiple price paths using:
  - Geometric Brownian Motion
  - Poisson-driven Jump Diffusion
- ✅ Calculates:
  - Value at Risk (VaR)
  - Conditional VaR (CVaR / Expected Shortfall)
- ✅ Detects price jumps based on standard deviation cutoff
- ✅ Visualizes:
  - Simulated price paths
  - Histogram of final simulated prices with VaR overlay
- ✅ Saves:
  - Price path simulations
  - Jump event logs
  - Summary statistics

---

## 📁 Project Structure

├── main.ipynb # Jupyter notebook for running simulations
├── data/
│ ├── AAPL_price_paths.csv # Simulated price paths
│ ├── AAPL_jumps.csv # Historical jump detection log
│ └── AAPL_summary.csv # Summary of simulation and risk metrics
├── modules/
│ ├── simulation.py # Monte Carlo simulation functions
│ ├── risk_metrics.py # VaR, CVaR calculations
│ └── jump_detection.py # Jump detection and statistics
---

## 🧪 How It Works

1. **Fetch Stock Data**  
   User provides a stock ticker, date range, and simulation preferences.

2. **Jump Detection**  
   Log returns are analyzed to identify statistical jumps beyond a defined σ-cutoff.

3. **Monte Carlo Simulation**  
   Thousands of future paths are simulated incorporating both drift, volatility, and jump events.

4. **Risk Calculation**  
   From simulated ending prices:
   - `VaR` is estimated at a user-defined confidence level
   - `CVaR` is the average of losses beyond the VaR threshold

5. **Data Export and Visualization**  
   Results are plotted and optionally saved to CSV files for further analysis.

---

## 📌 Example Output

**Exports**
- `data/GFS_price_paths.csv` — Simulated prices for all trials
- `data/GFS_jumps.csv` — Dates where return jumps exceeded threshold
- `data/GFS_summary.csv` — Summary stats (VaR, CVaR, lambda, etc.)

---

## ✏️ User Inputs

- **Ticker**: Stock symbol (e.g., `AAPL`, `MSFT`)
- **Date Range**: Start and end date for historical data
- **Simulation Days**: Number of future trading days to simulate (e.g., 1, 5, 30)
- **Trials**: Number of Monte Carlo trials (e.g., 1000, 10,000)
- **Confidence Level**: For VaR and CVaR (e.g., 0.90, 0.95)

---

## 📦 Requirements

```bash
pip install yfinance numpy pandas matplotlib seaborn scipy tabulate