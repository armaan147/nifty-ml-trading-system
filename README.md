# ML-Assisted Intraday Trading System on NIFTY

## Project Summary

This project presents an end-to-end intraday trading framework built using NIFTY spot data. 
The focus is on designing a stable and interpretable trading system rather than short-term 
price prediction.

A reusable data pipeline is used to clean and validate high-frequency market data. 
Interpretable signals representing trend direction, momentum change, and market stability 
are constructed and used to define a baseline EMA crossover strategy. While the baseline 
strategy captures trending phases, it shows instability during sideways markets.

To improve robustness, a machine learning–based trade filtering layer is introduced. 
The model acts as a decision-support mechanism to selectively allow or skip trades rather 
than forecast prices. Market regimes are also identified using both rule-based logic and 
probabilistic methods, enabling regime-aware trade execution.

Results show that layered filtering using machine learning and regime awareness reduces 
drawdowns and improves overall stability compared to the baseline strategy. Outlier analysis 
further highlights that a small number of extreme trades contribute disproportionately to 
gains and losses, reinforcing the importance of contextual filtering.

## Installation
pip install -r requirements.txt

## How to run
Run notebooks sequentially from the notebooks/ directory.
Each notebook saves outputs used by downstream analysis.

## Data Description
- Instrument: **NIFTY 50 Index**
- Frequency: **Intraday (5-minute bars)**
- Source: **Yahoo Finance**
- Scope: Limited intraday history due to free data constraints

The emphasis is on **methodology and correctness**, not data volume.


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


## Baseline Trading Strategy
A simple **EMA crossover strategy** is used as the baseline.

### Logic
- Long when EMA(5) > EMA(15)
- Short when EMA(5) < EMA(15)
- Trades executed on the next candle to avoid look-ahead bias

This strategy serves as a reference point to evaluate whether ML or regime filters
actually add value.


## Machine Learning Trade Filter
Rather than predicting price direction directly, ML is framed as a **binary filtering
problem**:

> *Should the next trade be taken or skipped?*

### ML Setup
- Model: Logistic Regression
- Features: EMA(5), EMA(15), Returns
- Train/Test Split: Time-ordered (70% / 30%)
- Class balancing enabled

## Regime Analysis (Rule-Based)
To reduce over-trading during noisy conditions, a simple regime classification is added:

- Rolling mean of returns → trend direction
- Rolling volatility → noise level

Regimes are classified as:
- Uptrend
- Downtrend
- Sideways

Trades are restricted to trend-consistent regimes only.

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

## Outlier Trade Analysis
To understand where most gains or losses originate, an outlier analysis is performed on
trade returns using z-score thresholds.

This helps identify:
- Extreme trades
- Regime conditions associated with large moves
- Strategy sensitivity to rare events

### Feature Enhancements
Additional derived features such as EMA slopes, rolling return statistics,
and volatility ratios were introduced as proxies for market dynamics.
Greeks and IV were not directly computed due to lack of reliable options data,
but the framework supports their future integration.


## Limitations
- No options or futures data due to API constraints
- Limited intraday history
- No transaction cost modeling

## Future Improvements
- Incorporate volatility-based position sizing
- Add options/futures data and derived features
- Experiment with tree-based or sequence models
- Expand regime analysis with longer historical data

## Project Structure
data/      – datasets and reports
notebooks/ – analysis notebooks
src/       – reusable python modules
models/    – saved trained models
results/   – strategy summaries
plots/     – visual outputs

## Author
**Armaan Yadav**

