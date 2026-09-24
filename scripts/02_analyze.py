import pandas as pd

df = pd.read_csv('data/clean_data/data_that_has_been_cleaned.csv')

print("The average length of a bike ride: ")

print(df.groupby('member_casual')['ride_length'].mean())

print("\nDays of the week:")

print(df.groupby(['member_casual','day_of_week'])['day_of_week'].count())

