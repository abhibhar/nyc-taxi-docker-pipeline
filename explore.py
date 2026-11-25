import pandas as pd

url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

df = pd.read_csv(
    url,
    nrows=100,
    parse_dates=["tpep_pickup_datetime", "tpep_dropoff_datetime"]
)

print(df.dtypes)
print()
df["duration"] = df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]
print(df[["tpep_pickup_datetime", "tpep_dropoff_datetime", "duration"]].head())
