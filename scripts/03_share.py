import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/clean_data/data_that_has_been_cleaned.csv')

#first graphic: mean duration of courses
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='member_casual', y='ride_length')
plt.title('Mean duration of courses: Members vs. Casuals')
plt.ylabel('Minutes')
plt.xlabel('Users')
plt.show()

#second graphic: no. of courser per week
plt.figure(figsize=(10,6))
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sns.countplot(data=df,x='day_of_week',hue='member_casual',order=days)
plt.title('No. of coursers in a week')
plt.ylabel('No. of courses')
plt.xlabel('Days of the week')
plt.show()
