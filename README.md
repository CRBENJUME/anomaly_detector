# 📈 Quantitative Anomaly Detection & Trading Volatility Script

Welcome to the **Quantitative Anomaly Detector** repository! This project implements a quantitative finance pipeline using Python to download high-frequency financial data, compute logarithmic returns, apply rolling statistical metrics, and automatically detect market anomalies or breakout signals using standard deviation thresholds.

---

## 🚀 Project Overview

The core script downloads intraday price action from Yahoo Finance, models volatility dynamically using rolling windows, and flags statistically significant upward and downward anomalies (similar to Bollinger Band breakouts on returns).

Key highlights of the script include:
* **Automated Data Fetching**: Pulls high-frequency intraday financial time-series data via `yfinance`.
* **Logarithmic Returns**: Computes stationary log returns ($\ln(P_t / P_{t-1})$) for rigorous quantitative analysis.
* **Rolling Volatility Bands**: Calculates moving averages and rolling standard deviations to establish adaptive upper and lower thresholds.
* **Anomaly Flagging**: Automatically isolates data points exceeding user-defined standard deviation boundaries ($k=2$).
* **Data Visualization**: Generates a clean, comprehensive `matplotlib` chart plotting return distribution alongside visual markers for buy/sell or bullish/bearish anomalies.

---

## 📊 Data Sources & Methodology

* **yfinance**: Primary data interface for historical market feeds (configured by default for NASDAQ 100 index futures/ETF proxy `^NDX` at 1-minute intervals over a 2-day period).
* **Mathematical Formulas**:
  * **Log Returns**: $r_t = \ln\left(\frac{P_t}{P_{t-1}}\right)$
  * **Rolling Mean**: $\mu_t = \frac{1}{W} \sum_{i=0}^{W-1} r_{t-i}$
  * **Rolling Standard Deviation**: $\sigma_t = \sqrt{\frac{1}{W} \sum_{i=0}^{W-1} (r_{t-i} - \mu_t)^2}$
  * **Thresholds**: $\text{Thresholds}_t = \mu_t \pm (k \cdot \sigma_t)$

---

## 🏁 How It Works (`anomaly_detector.py`)

1. **Data Ingestion**: Downloads short-term intraday OHLCV time-series records for the target asset.
2. **Feature Engineering**: Derives logarithmic price changes to normalize asset variance.
3. **Statistical Windowing**: Applies a rolling window ($W=50$) to compute localized mean and volatility boundaries.
4. **Classification**: 
   * `Anomaly = 1`: Bullish spike where log return exceeds the upper volatility band.
   * `Anomaly = -1`: Bearish plunge where log return breaches the lower volatility boundary.
5. **Plotting**: Maps the entire sequence with customized color-coded scatter points for instant visual inspection.

---

## 🛠️ Dependencies

Make sure you have the required quantitative and plotting Python packages installed:

```bash
pip install numpy pandas yfinance matplotlib
```
## 📁 File Structure

* `anomaly_detector.py` — Main quantitative script handling data download, statistical vectorization, anomaly classification, and Matplotlib figure generation.

---

## 🔧 Usage

You can customize the asset ticker, timeframe interval, historical period, rolling window size, or standard deviation multipliers directly in the configuration section of the script:

```python
symbol = "^NDX"
intervalo = "1m"
periodo = "2d"
window = 50   # Rolling window size
k = 2         # Standard deviation multiplier
```
## 📊 Sample Output Visualization Description

The script outputs an interactive `matplotlib` plot containing:
* **Gray Line**: Continuous log return fluctuations over the selected timeframe.
* **Dashed Lines**: Brown upper threshold (Venta / Overbought zone) and green lower threshold (Compra / Oversold zone).
* **Colored Scatter Points**:
  * 🟠 **Orange Dots**: Bullish anomalies exceeding the upper volatility boundary.
  * 🔴 **Red Dots**: Bearish anomalies dropping below the lower volatility boundary.

---

## 📈 Quantitative Applications

* **Volatility Breakouts**: Identify sudden liquidity spikes or news-driven market shocks.
* **Algorithmic Strategy Prototyping**: Serve as a foundational logic filter for mean-reversion or momentum-based trading backtests.
* **Risk Management**: Quantify high-frequency tail risks and market anomalies dynamically.

---

🚀 *Start exploring quantitative finance and market dynamics with Python!*
