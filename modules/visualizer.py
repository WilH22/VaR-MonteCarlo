import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from scipy.stats import norm
import seaborn as sns
from tabulate import tabulate

def plot_price_paths(ticker, price_paths: np.ndarray):
    df = pd.DataFrame(price_paths)
    plt.figure(figsize=(12, 6))
    plt.plot(df)
    
    # Auto adjustment Axis for better visuals
    plt.xlim(0, df.shape[0] - 1)
    plt.ylim(df.min().min() * 0.95, df.max().max() * 1.05)

    plt.title(f"Simulated Price Paths - {ticker}")
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.grid(True)
    plt.tight_layout()
    filename = f"{ticker}_Simulated_Price_Paths.png"
    plt.savefig(f"VaR-MonteCarlo/data/{filename}", dpi=300, bbox_inches='tight')
    plt.show(block=False)
    plt.close()

def plot_var(ticker, ending_prices, VaR_price, confidence_level):
    plt.figure(figsize=(10, 5))
    sns.histplot(ending_prices, kde=True, color="skyblue", bins=50)
    plt.axvline(VaR_price, color='red', linestyle='--',
                label=f"{int(confidence_level*100)}% VaR = ${VaR_price:.2f}")
    plt.title(f"Distribution of Final Simulated Prices - {ticker}")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    filename = f"{ticker}_Distribution_of_Final_Simulated_Prices.png"
    plt.savefig(f"VaR-MonteCarlo/data/{filename}", dpi=300, bbox_inches='tight')
    plt.show(block=False)
    plt.close()