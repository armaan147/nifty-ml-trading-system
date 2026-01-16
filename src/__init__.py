import pandas as pd

def load_csv(path):
    df = pd.read_csv(path)
    df.columns = [c.strip() for c in df.columns]
    return df
