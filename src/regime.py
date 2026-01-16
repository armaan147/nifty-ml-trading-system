def classify_regime(row):
    if row["Rolling_Return"] > 0 and row["Rolling_Volatility"] < 0.002:
        return "Uptrend"
    elif row["Rolling_Return"] < 0 and row["Rolling_Volatility"] < 0.002:
        return "Downtrend"
    else:
        return "Sideways"
