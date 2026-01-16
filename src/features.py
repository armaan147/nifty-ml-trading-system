def add_ema_features(df, short_span=5, long_span=15):
    df["EMA_5"] = df["Close"].ewm(span=short_span, adjust=False).mean()
    df["EMA_15"] = df["Close"].ewm(span=long_span, adjust=False).mean()
    return df

def add_returns(df):
    df["Returns"] = df["Close"].pct_change()
    return df
