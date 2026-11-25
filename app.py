import sys
import pandas as pd

month = int(sys.argv[1])
df = pd.DataFrame({"day": [1, 2, 3], "sales": [100, 250, 175]})
df["month"] = month
print(df)

df.to_csv(f"output/sales_{month}.csv", index=False)
print(f"Saved output/sales_{month}.csv")