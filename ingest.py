import pandas as pd
from sqlalchemy import create_engine

url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
engine = create_engine("postgresql+psycopg://root:root@mydb:5432/sales")

chunks = pd.read_csv(
    url,
    parse_dates=["tpep_pickup_datetime", "tpep_dropoff_datetime"],
    chunksize=100000,
    low_memory=False,
)

total = 0
for i, chunk in enumerate(chunks):
    mode = "replace" if i == 0 else "append"
    chunk.to_sql("yellow_taxi", engine, if_exists=mode, index=False)
    total += len(chunk)
    print(f"chunk {i + 1}: loaded {total} rows")

print("DONE:", total)
