def ema_crossover_signal(df):
    df["Signal"] = 0
    df.loc[df["EMA_5"] > df["EMA_15"], "Signal"] = 1
    df.loc[df["EMA_5"] < df["EMA_15"], "Signal"] = -1
    return df
