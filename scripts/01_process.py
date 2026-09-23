import pandas as pd
import glob
from pathlib import Path

# defining the path to the data
folder = Path("data/raw_data")

# looking for ALL .csv files
csv_files = list(folder.glob("*.csv"))

# reading all the files in a list
df_list = [pd.read_csv(filename) for filename in csv_files]

# concatenating all the files into one dataframe 
df = pd.concat(df_list,ignore_index=True)

#print("Info:")
#print(df.info())

#changing the data type to date instead of string
print("It takes a lil bit of time...")
df['started_at'] = pd.to_datetime(df['started_at'])
df['ended_at'] = pd.to_datetime(df['ended_at'])

# calculating and creating a new column, ride_length
df['ride_length'] = (df['ended_at']-df['started_at']).dt.total_seconds() / 60

# new column: day of the week
df['day_of_week'] = df['started_at'].dt.day_name()

# cleaning process: dropping the stations where the names dont show up
df_clean = df.dropna(subset=['start_station_name', 'end_station_name'])

# and where the ride is negative
df_clean = df_clean[df_clean['ride_length'] > 0]

# saving the cleaned dataset
saving_route = Path("data/clean_data/data_that_has_been_cleaned.csv")

df_clean.to_csv(saving_route, index = False)

print(f'\nDone! Length of the dataset now: {len(df_clean)}')
