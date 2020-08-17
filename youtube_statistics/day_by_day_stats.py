import random
import matplotlib.pyplot as plt
import pandas as pd
from youtube_statistics import config
import os
from datetime import datetime
import time

PLOT_NUMBER = datetime.now().strftime('%d-%m-%Y')

df = pd.read_csv(config.DATA_FILE, parse_dates=['date'])

#formatiing the date
df['date'] = pd.to_datetime(df.date)
df['date'] = df['date'].dt.strftime('%d/%m/%y')


PLOT_DIR = os.path.join(config.SCREENSHOT_DIR, 'plots')

def totalViewOnDayByDay(df):
    return df.groupby(['date'], sort=False).sum()

def lessonGroupedViews(df):
    pass

FIG_NAME = os.path.join(PLOT_DIR, str(PLOT_NUMBER)+'-totalViewOnDayByDay.png')
print(FIG_NAME)
sumDf = totalViewOnDayByDay(df)
sumDf.plot(kind='bar', figsize=(17, 10),  rot=0)
plt.xticks(rotation=45)
plt.title("Total Views Count per Day  | Udacity")
# plt.savefig(FIG_NAME, bbox_inches='tight')
# plt.show()



def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

number_of_colors = len(df['date'].unique())

colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
print(colors)

print(df.head())


# df_pivoted = df.pivot(index='lesson', columns='date', values='views')
#
# df_pivoted.plot(kind='bar', figsize=(40, 10), color=colors, rot=0, width=0.7,align='center')
# plt.title("Historical Count of Views: Day by Day Comparison | Udacity")
# plt.xlabel("Lessons", labelpad=16)
# plt.ylabel("Count", labelpad=16)
#
# FIG_NAME = os.path.join(PLOT_DIR, 'Historical-'+str(PLOT_NUMBER)+'.png')
# # plt.savefig(FIG_NAME, dpi=300, bbox_inches='tight')
# plt.show()
# #


def format_lesson(lesson):
    return str(lesson).split('-')[0]

df['lesson'] = df['lesson'].apply(lambda x: format_lesson(x))


def plot(dataframe, fun):
    print(dataframe.head())

    df_pivoted = dataframe.pivot(index='lesson', columns='date', values='views').sort_index(axis=1, level=1)

    sorted_date_columns = list(df_pivoted.columns.values)
    sorted_date_columns.sort(key=lambda x: time.mktime(time.strptime(x, "%d/%m/%y")))

    df_pivoted = df_pivoted.reindex(columns=sorted_date_columns)
    # data = data.sort_index()
    print(df_pivoted.head())

    df_pivoted.plot(kind='bar', figsize=(40, 10), color=colors, rot=0, width=0.7, align='center')
    if fun == 'sum':
        plt.title("Historical Count of Views: Day by Day Comparison | Udacity")
    else:
        plt.title("Historical Progress of Azure ML: Day by Day Comparison | Udacity")

    plt.xlabel("Lessons", labelpad=16)
    plt.ylabel("Count", labelpad=16)

    if fun == 'sum':
        FIG_NAME = os.path.join(PLOT_DIR, 'Historical-' + str(PLOT_NUMBER) + '.png')
    else:
        FIG_NAME = os.path.join(PLOT_DIR, 'Historical-MEAN-' + str(PLOT_NUMBER) + '.png')

    plt.savefig(FIG_NAME, dpi=300, bbox_inches='tight')
    plt.show()





# df = df.groupby(['date','lesson']).sum()
generalizeDf = df.groupby(['date', 'lesson'], sort=False).sum().reset_index()
#used sort=False because using groupby it changes the indexes

plot(generalizeDf, fun='sum')

generalizeDf = df.groupby(['date', 'lesson'], sort=False).mean().reset_index()

plot(generalizeDf, fun='mean')