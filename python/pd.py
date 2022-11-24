import pandas as pd
import numpy as np

path = "https://github.com/dongupak/DataML/raw/main/csv/"
file = path + "vehicle_prod.csv"

df = pd.read_csv(file, index_col = 0)
SUM = df.sum(axis = 1)
MEAN = df.mean(axis = 1)

df["total"] = SUM
df["mean"] = MEAN

print(df.head(3))