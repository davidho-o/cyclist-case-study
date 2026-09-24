import pandas as pd

df = pd.read_csv('data/clean_data/data_that_has_been_cleaned.csv')

print("\nThe average length of a bike ride: ")

average_length = df.groupby('member_casual')['ride_length'].mean()

print(average_length)

print("\nDays of the week:")

days_of_the_week_use = df.groupby(['member_casual','day_of_week'])['day_of_week'].count()

print(days_of_the_week_use)

busiest_day_members = days_of_the_week_use['member'].idxmax()
print(f"\nThe busiest day for members is: {busiest_day_members}")

busiest_day_casuals = days_of_the_week_use['casual'].idxmax()
print(f"\nThe busiest day for casuals is: {busiest_day_casuals}")
