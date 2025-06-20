import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from scipy.stats import norm
import seaborn as sns
from tabulate import tabulate

from modules.data_loader import fetch_stock_data
from modules.calculation import compute_parameters
from modules.calculation import detect_jumps
from modules.simulation import simulate_price_paths
from modules.visualizer import plot_price_paths
from modules.calculation import compute_VaR_CVaR
from modules.visualizer import plot_var
from modules.data_loader import summary_data

# Step 1: Input and Fetch stock data
ticker = input("Enter stock ticker (e.g., AAPL): ").strip().upper()
start = input("Enter start date (YYYY-MM-DD): ").strip()
end = input("Enter end date (YYYY-MM-DD or leave blank for today's date): ").strip() or None

print("\n🗓️ How many future days do you want to simulate?")
print("Typical values: 1 for daily VaR, 5 for weekly, 10–30 for longer-term risk")
days = int(input("Enter number of simulation days: "))

print("\n🔁 How many simulation trials should we run?")
print("Typical values: 1000 for quick test, 10,000 for good accuracy, 50,000+ for production")
trials = int(input("Enter number of trials (simulated paths): "))

print(f"\n📈 Running simulation for {ticker} from {start} to {end or 'latest'}...")
data=fetch_stock_data(ticker, start, end)

# Step 2: Compute log returns and model parameters
log_returns, drift, stdev = compute_parameters(data)

# Step 3: Calculate jump parameters 
use_auto_jump = input("Do you want to auto-detect jumps? (y/n): ").strip().lower()

if use_auto_jump == "y":
    sigma_cutoff_input = input("Input your sigma cutoff (default = 3): ").strip()
    sigma_cutoff = float(sigma_cutoff_input) if sigma_cutoff_input else 3.0

    total_days, total_jumps, jump_df, lambda_, mu_j, sigma_j = detect_jumps(log_returns, sigma_cutoff)
    print(f"\n✅ Auto-detected {total_jumps} jumps over {total_days} trading days")
    print("📈 Simulating Price Paths using GBM with Jump Diffusion Model")

else:
    # Manual input mode
    avg_jump_input = input("Enter average jumps per year (e.g., 2.0, default = 0): ").strip()
    lambda_ = float(avg_jump_input) if avg_jump_input else 0

    if lambda_ != 0:
        mu_j_input = input("Enter average jump size (mu_j), e.g., -0.02 (default = -0.02): ").strip()
        sigma_j_input = input("Enter jump volatility (sigma_j), e.g., 0.10 (default = 0.10): ").strip()

        mu_j = float(mu_j_input) if mu_j_input else -0.02
        sigma_j = float(sigma_j_input) if sigma_j_input else 0.10
        print("\n✏️  Manual input of jump parameters accepted")
        print("📈 Simulating Price Paths using GBM with Jump Diffusion Model")

    else:
        mu_j = 0
        sigma_j = 0
        print("\n📉 No jumps will be included (lambda = 0)")
        print("📈 Simulating Price Paths using standard GBM")

    jump_df = None
    total_days = len(log_returns)
    total_jumps = int(lambda_ * total_days / 252)

# Step 4: Simulate price paths (Jump Diffusion Model)
price_paths = simulate_price_paths(data, drift, stdev, days, trials, lambda_, mu_j, sigma_j)

# Step 5: Plot price paths
plot_price_paths(price_paths)

#Step 6: Calculate Expected Value at Risk (VaR) and Shortfall (CVaR)
print("\n🔒 Enter your desired confidence level for VaR calculation.") #default will take CI =0.95
print("   Typical values: 0.90 for 90%, 0.95 for 95%")
confidence_level = float(input("Enter confidence level (e.g., 0.95): ") or 0.95)

ending_prices,VaR_price,CVaR = compute_VaR_CVaR(price_paths, confidence_level)
print()
S0 = price_paths[0, 0]
print(f"📌 Initial Price(S₀) on {end}: ${S0:.2f}")
print(f"📉 {int(confidence_level*100)}% VaR: ${VaR_price:.2f}")
print(f"💥 Expected Shortfall (CVaR): ${CVaR:.2f}")

#Step 7: Plot VaR in Histogram
plot_var(ending_prices, VaR_price, confidence_level)

#Step 8: Tabulate the data 
summary_df = summary_data(ticker, start, end, S0, price_paths, confidence_level,
                          VaR_price, CVaR, lambda_, mu_j, sigma_j, total_days, total_jumps)
summary_df_transposed = summary_df.T.reset_index() # Transpose and reset index for export
summary_df_transposed.columns = ['Metric', 'Value']
print("\n📊 Summary Table:")
print(tabulate(summary_df.T, headers=["Metric", "Value"], tablefmt="fancy_grid"))

save_csv = input("Save results to CSV? (y/n): ").strip().lower() == 'y'

if save_csv:
    files_to_save = {
        "jumps": jump_df,
        "price_paths": price_paths,
        "summary": summary_df_transposed
    }

    for name, df in files_to_save.items():
        # Convert to DataFrame if it's a NumPy array
        if isinstance(df, np.ndarray):
            df = pd.DataFrame(df)

        filename = f"data/{ticker}_{name}.csv"
        df.to_csv(filename, index=False)
        print(f"📄 {name.replace('_', ' ').title()} data saved to {filename}")
        print()  # extra newline
else:
    pass
