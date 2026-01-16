# ML-Assisted Intraday Trading System on NIFTY

## Overview
This project explores how machine learning and regime analysis can be used to support
a traditional technical trading strategy in an intraday setting.

Instead of trying to “predict the market”, the focus is on building a clean,
explainable pipeline where ML and regime detection act as filters on a baseline
strategy. The goal is to understand *when* a strategy should trade rather than *forcing*
directional accuracy.

The entire system is built end-to-end from raw data collection to strategy comparison.

---

## Data Description
- Instrument: **NIFTY 50 Index**
- Frequency: **Intraday (5-minute bars)**
- Source: **Yahoo Finance**
- Scope: Limited intraday history due to free data constraints

The emphasis is on **methodology and correctness**, not data volume.

---

## Data Processing Pipeline
The project follows a clear and reproducible pipeline:

1. **Data Collection**
   - Raw intraday price data downloaded and stored locally.

2. **Data Preprocessing**
   - Duplicate rows removed
   - Missing values handled conservatively
   - Numeric columns enforced to avoid downstream errors

3. **Feature Construction**
   - EMA (5-period)
   - EMA (15-period)
   - Percentage returns

The final feature dataset is saved and reused across all strategy notebooks.

---

## Baseline Trading Strategy
A simple **EMA crossover strategy** is used as the baseline.

### Logic
- Long when EMA(5) > EMA(15)
- Short when EMA(5) < EMA(15)
- Trades executed on the next candle to avoid look-ahead bias

This strategy serves as a reference point to evaluate whether ML or regime filters
actually add value.

---

## Machine Learning Trade Filter
Rather than predicting price direction directly, ML is framed as a **binary filtering
problem**:

> *Should the next trade be taken or skipped?*

### ML Setup
- Model: Logistic Regression
- Features: EMA(5), EMA(15), Returns
- Train/Test Split: Time-ordered (70% / 30%)
- Class balancing enabled
---

## Regime Analysis (Rule-Based)
To reduce over-trading during noisy conditions, a simple regime classification is added:

- Rolling mean of returns → trend direction
- Rolling volatility → noise level

Regimes are classified as:
- Uptrend
- Downtrend
- Sideways

Trades are restricted to trend-consistent regimes only.

---

## HMM-Based Regime Detection
To align more closely with real-world quantitative approaches, a **Hidden Markov Model
(HMM)** is used to infer latent market regimes.

### HMM Details
- Observations: Returns and rolling volatility
- States: 3 latent regimes
- Interpretation:
  - Positive return state → Uptrend
  - Negative return state → Downtrend
  - Neutral state → Sideways

The HMM regime is then used to **control when EMA trades are allowed**.

---

## Strategy Comparison
Three strategies are compared on the same dataset:

1. Baseline EMA strategy  
2. ML-filtered EMA strategy  
3. HMM-filtered EMA strategy  

The comparison focuses on:
- Equity curve behavior
- Trade selectivity
- Noise reduction

Rather than maximizing returns, the emphasis is on **understanding how filters change
strategy behavior**.

---

## Outlier Trade Analysis
To understand where most gains or losses originate, an outlier analysis is performed on
trade returns using z-score thresholds.

This helps identify:
- Extreme trades
- Regime conditions associated with large moves
- Strategy sensitivity to rare events
---

## Limitations
- No options or futures data due to API constraints
- Limited intraday history
- No transaction cost modeling
---

## Future Improvements
- Incorporate volatility-based position sizing
- Add options/futures data and derived features
- Experiment with tree-based or sequence models
- Expand regime analysis with longer historical data

---

## Author
**Armaan Yadav**

