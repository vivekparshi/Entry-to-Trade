import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_fibonacci_retracement(high, low):
    distance = high - low
    level_0 = high
    level_23_6 = high - distance * 0.236
    level_38_2 = high - distance * 0.382
    level_50 = high - distance * 0.5
    level_61_8 = high - distance * 0.618
    level_100 = low

    return level_0, level_23_6, level_38_2, level_50, level_61_8, level_100

def analyze_trend(prices):
    ma_50 = np.mean(prices[-50:])
    ma_200 = np.mean(prices[-200:])

    if ma_50 > ma_200:
        return "Uptrend"
    elif ma_50 < ma_200:
        return "Downtrend"
    else:
        return "Sideways"

def plot_chart(prices, fib_levels):
    plt.figure(figsize=(12, 6))
    plt.plot(prices, color='blue', label='Price')

    for level, value in fib_levels.items():
        plt.axhline(y=value, color='red', linestyle='--', label=f'{level}%')

    plt.xlabel('Period')
    plt.ylabel('Price')
    plt.title('Price Chart with Fibonacci Retracement Levels')
    plt.legend()
    plt.grid(True)
    plt.show()

prices = [120, 110, 130, 100, 115, 105, 125, 95, 120]

high = max(prices)
low = min(prices)
fib_levels = {
    'Level 0': high,
    'Level 23.6': high - (high - low) * 0.236,
    'Level 38.2': high - (high - low) * 0.382,
    'Level 50': high - (high - low) * 0.5,
    'Level 61.8': high - (high - low) * 0.618,
    'Level 100': low
}
trend = analyze_trend(prices)
plot_chart(prices, fib_levels)
print(f"FIBONACCI RETRACEMENT LEVELS:")
for level, value in fib_levels.items():
    print(f"{level}: {value}")
print(f"Trend: {trend}")
