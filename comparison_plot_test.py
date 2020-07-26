import matplotlib.pyplot as plt
import pandas as pd

udacity_stats = {
    "date": ['2020', '2019', '2018', '2019'],
    'lessons': [1.1, 1.1, 1.1, 1.2],
    'views': [9000, 8800, 8000, 7200]
}

df = pd.DataFrame(udacity_stats)

months_in_order = df['lessons'].values
df_flights_pivoted = df.pivot(index='lessons', columns='date', values='views')
print(df_flights_pivoted.head())
# df_flights_pivoted = df.pivot(index='lessons', columns=   'date', values='views').reindex(months_in_order)

df_flights_pivoted.plot(kind='bar', figsize=(17, 10), color=['lightgray', 'gray', 'black'], rot=0)
plt.title("Historical Count of Views: Day by Day Comparison", y=1.013, fontsize=22)
plt.xlabel("Lessons", labelpad=16)
plt.ylabel("Count [Passengers]", labelpad=16)

df["period"] = df["date"].astype(str)  + ' ' + df["lessons"].astype(str)
print(df.head())
df.plot.barh(x='period', y='views')

plt.show()