import random
import matplotlib.pyplot as plt
import pandas as pd
from youtube_statistics import config

df = pd.read_csv(config.DATA_FILE)

print(df.head())

#formatiing the date
df['date'] = pd.to_datetime(df.date)
df['date'] = df['date'].dt.strftime('%d/%m/%Y')
print(df.head())

# def format_lesson(lesson):
#     return str(lesson).split('-')[0]
#
# df['lesson'] = df['lesson'].apply(lambda x: format_lesson(x))

# print(df.groupby(['date', 'lesson']).sum())

print(df.head())

print(df.groupby(['date', 'lesson']).sum())


# number_of_colors = 8
#
# color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
#              for i in range(number_of_colors)]