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

![image](https://github.com/user-attachments/assets/4ad8d00c-dcc8-4fa8-897d-cd385930b827)

---

## 🧪 How It Works

1. **Fetch Stock Data**  
   User provides a stock ticker, date range, and simulation preferences.
![image](https://github.com/user-attachments/assets/e4d38bad-bc00-4f53-816c-c35b34a74058)

2. **Jump Detection**  
   Log returns are analyzed to identify statistical jumps beyond a defined σ-cutoff.

3. **Monte Carlo Simulation**  
   Thousands of future paths are simulated incorporating both drift, volatility, and jump events.
![image](https://github.com/user-attachments/assets/45b25349-dc2c-4a62-8890-67977750b411)

4. **Risk Calculation**  
   From simulated ending prices:
   - `VaR` is estimated at a user-defined confidence level
   - `CVaR` is the average of losses beyond the VaR threshold
![image](https://github.com/user-attachments/assets/19138555-058e-49e6-a8b9-960f69bf0141)
![image](https://github.com/user-attachments/assets/c9317986-2772-43cf-9db2-d42196a12f80)


5. **Data Export and Visualization**  
![image](https://github.com/user-attachments/assets/fb2e5772-df56-4daf-86fd-c6c4951038aa)
Results are plotted and optionally saved to CSV files for further analysis.

---

## 📌 Example Output

**Exports**
- `data/{Ticker}_price_paths.csv` — Simulated prices for all trials
- `data/{Ticker}_jumps.csv` — Dates where return jumps exceeded threshold
- `data/{Ticker}_summary.csv` — Summary stats (VaR, CVaR, lambda, etc.)

---

## ✏️ User Inputs

- **Ticker**: Stock symbol (e.g., `AAPL`, `MSFT`)
- **Date Range**: Start and end date for historical data. If end date is NA, will take today's date
- **Simulation Days**: Number of future trading days to simulate (e.g., 1, 5, 30)
- **Trials**: Number of Monte Carlo trials (e.g., 1000, 10,000)
- **Confidence Level**: For VaR and CVaR (e.g., 0.90, 0.95)

---

## 📦 Requirements

```bash
pip install yfinance numpy pandas matplotlib seaborn scipy tabulate
