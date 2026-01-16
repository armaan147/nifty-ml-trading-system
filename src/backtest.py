def compute_strategy_returns(df, signal_col="Signal", return_col="Returns"):
    df["Strategy_Return"] = df[signal_col].shift(1) * df[return_col]
    df["Cumulative_Return"] = (1 + df["Strategy_Return"]).cumprod()
    return df
