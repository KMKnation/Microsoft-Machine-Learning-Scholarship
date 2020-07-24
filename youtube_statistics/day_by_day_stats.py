import random
import matplotlib.pyplot as plt
import pandas as pd
from youtube_statistics import config
import os
from datetime import datetime

PLOT_NUMBER = datetime.now().strftime('%d-%m-%Y')

df = pd.read_csv(config.DATA_FILE)

PLOT_DIR = os.path.join(config.SCREENSHOT_DIR, 'plots')

def totalViewOnDayByDay(df):
    df['date'] = pd.to_datetime(df.date)
    df['date'] = df['date'].dt.strftime('%d/%m/%Y')

    return df.groupby(['date']).sum()

def lessonGroupedViews(df):
    pass

FIG_NAME = os.path.join(PLOT_DIR, str(PLOT_NUMBER)+'-totalViewOnDayByDay.png')
print(FIG_NAME)
sumDf = totalViewOnDayByDay(df)
sumDf.plot(kind='bar', figsize=(17, 10),  rot=0)
plt.savefig(FIG_NAME)
# plt.show()




#formatiing the date
df['date'] = pd.to_datetime(df.date)
df['date'] = df['date'].dt.strftime('%d/%m/%Y')


# def format_lesson(lesson):
#     return str(lesson).split('-')[0]
#
# df['lesson'] = df['lesson'].apply(lambda x: format_lesson(x))


# df = df.groupby(['date','lesson']).sum()
# print(df.head())

def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

number_of_colors = len(df['date'].unique())

colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
print(colors)

print(df.head())


df_pivoted = df.pivot(index='lesson', columns='date', values='views')

df_pivoted.plot(kind='bar', figsize=(40, 10), color=colors, rot=0, width=0.7,align='center')
plt.title("Historical Count of Views: Day by Day Comparison | Udacity", y=1.513, fontsize=22)
plt.xlabel("Lessons", labelpad=16)
plt.ylabel("Count", labelpad=16)

FIG_NAME = os.path.join(PLOT_DIR, 'Historical-'+str(PLOT_NUMBER)+'.png')
plt.savefig(FIG_NAME, dpi=300)
plt.show()
#
