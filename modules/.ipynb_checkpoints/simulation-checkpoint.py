import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from scipy.stats import norm
import seaborn as sns
from tabulate import tabulate

def simulate_price_paths(data, drift, stdev, days, trials, lambda_, mu_j, sigma_j):
    Z = norm.ppf(np.random.rand(days, trials))
    dt= 1/252
    N = np.random.poisson(lambda_ * dt, size=(days, trials))  # 0 or 1 most of the time
    J = np.random.normal(mu_j, sigma_j, size=(days, trials))  # jump magnitude
    jumps = N * J
    daily_returns = np.exp(np.array(drift) + np.array(stdev) * Z + np.array(jumps))
    
    price_paths = np.zeros_like(daily_returns)
    price_paths[0] = data['Close'].iloc[-1]
    
    for t in range (1,days):
        price_paths[t] = price_paths[t-1]*daily_returns[t]
    
    return price_paths