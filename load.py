import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://root:root@mydb:5432/sales")

df = pd.DataFrame({
    "day": [3, 4, 5],
    "amount": [300, 120, 410]
})

df.to_sql("sales", engine, if_exists="append", index=False)
print("Loaded", len(df), "rows")