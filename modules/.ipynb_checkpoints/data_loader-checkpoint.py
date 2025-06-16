import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from scipy.stats import norm
import seaborn as sns
from tabulate import tabulate

def fetch_stock_data(ticker: str, start: str, end: str = None):
    data = yf.download(ticker, start=start, end=end, auto_adjust=True)
    return data

def summary_data(ticker,start,end,S0,price_paths,confidence_level,VaR_price,CVaR,lambda_,mu_j,sigma_j,total_days,total_jumps):
    summary_data = {
        "Ticker": ticker,
        "Start_Date": start,
        "End_Date": end if end else "latest",
        "Initial_Price": round(S0, 2),
        "Days_Simulated": price_paths.shape[0],
        "Trials": price_paths.shape[1],
        f"VaR_{int(confidence_level * 100)}%": round(VaR_price, 2),
        "CVaR": round(CVaR, 2),
        "Lambda_JumpsPerYear": round(lambda_, 3),
        "Mu_JumpMean": round(mu_j, 5),
        "Sigma_JumpStd": round(sigma_j, 5),
        "Total_Days_Observed": total_days,
        "Total_Jumps_Observed": total_jumps
    }
    summary_df = pd.DataFrame([summary_data])
    return(summary_df)