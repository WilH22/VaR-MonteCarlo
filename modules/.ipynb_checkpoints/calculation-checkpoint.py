import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from scipy.stats import norm
import seaborn as sns
from tabulate import tabulate

def compute_parameters(data: pd.DataFrame):
    log_returns = np.log(1+data['Close'].pct_change())
    mu = log_returns.mean()
    var = log_returns.var()
    drift = mu - (0.5*var)
    stdev = log_returns.std()
    return log_returns, drift, stdev

def detect_jumps(log_returns: pd.Series, sigma_cutoff: float = 3):
    log_returns = log_returns.squeeze()
    mu = log_returns.mean()
    sigma = log_returns.std()
    threshold = sigma_cutoff * sigma
    jump_mask = (np.abs(log_returns - mu) > threshold)
    jump_returns = log_returns[jump_mask]
    total_days = len(log_returns)
    total_jumps = int(jump_mask.sum())
    years = total_days / 252
    lambda_ = total_jumps / years if years > 0 else 0
    mu_j = jump_returns.mean() if total_jumps > 0 else 0
    sigma_j = jump_returns.std() if total_jumps > 0 else 0
    jump_df = pd.DataFrame({
        "Date": log_returns.index,
        "LogAdjReturn": log_returns.values,
        "Jump": jump_mask.astype(int)
    })
    return total_days,total_jumps,jump_df, lambda_, mu_j, sigma_j

def compute_VaR_CVaR(price_paths: np.ndarray, confidence_level):
    ending_prices = price_paths[-1, :]
    VaR_price = np.percentile(ending_prices, (1 - confidence_level) * 100)
    shortfall = ending_prices[ending_prices <= VaR_price]
    CVaR = np.mean(shortfall)
    return ending_prices,VaR_price,CVaR