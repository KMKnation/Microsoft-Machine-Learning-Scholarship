import os

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from youtube_statistics import config
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.animation as animation


df = pd.read_csv(config.DATA_FILE, parse_dates=['date'])

# formatiing the date
df['date'] = pd.to_datetime(df.date)
df['date'] = df['date'].dt.strftime('%d/%m/%y')

def change_width(ax, new_value) :
    for patch in ax.patches :
        current_width = patch.get_width()
        diff = current_width - new_value

        # we change the bar width
        patch.set_width(new_value)

        # we recenter the bar
        patch.set_x(patch.get_x() + diff * .2)


fig, ax = plt.subplots()


def compare_dayt_by_day(dataframe, date):

    dataframe = dataframe[dataframe['date'] == str(date)]

    vals = len(dataframe.values)

    if vals > 0:


        ax = sns.barplot(data=dataframe
                    , x='lesson'
                    , y='views'
                    , color='#02b3e4'
                    , ci=None
                    )

        columns_len = len(dataframe['lesson'].unique())
        plt.setp(ax.patches, linewidth=0)

        plt.title('Youtube Statistics | Microsoft Azure ML | Udacity | Day: {}'.format(date))
        change_width(ax, .35)

        fontsize =  400 / columns_len

        # plt.xticks(fontsize=6)
        fig = matplotlib.pyplot.gcf()
        # fig.set_size_inches(18.5, 10.5)
        # fig.set_size_inches(28.5, 50.5)
        plt.xticks(rotation=45, fontsize=fontsize)
        plt.grid(True)
        plt.draw()
        # plt.show()
    else:
        plt.draw()

def compare_last_chapters(dataframe, date):

    dataframe = dataframe[dataframe['lesson'].isin(
        ['7-0', '7-1', '7-2', '7-3''7-4', '7-5', '7-6', '7-7', '7-8', '7-9', '8-0', '8-1'])].reset_index()
    dataframe = dataframe[dataframe['date'] == str(date)]

    vals = len(dataframe.values)

    if vals > 0:


        ax = sns.barplot(data=dataframe
                    , x='lesson'
                    , y='views'
                    , color='#02b3e4'
                    , ci=None
                    )

        columns_len = len(dataframe['lesson'].unique())
        plt.setp(ax.patches, linewidth=0)

        plt.title('Youtube Statistics | Microsoft Azure ML | Udacity | Day: {}'.format(date))
        change_width(ax, .35)

        fontsize =  100 / columns_len

        # plt.xticks(fontsize=6)
        fig = matplotlib.pyplot.gcf()
        # fig.set_size_inches(18.5, 10.5)
        # fig.set_size_inches(28.5, 50.5)
        plt.xticks(rotation=45, fontsize=fontsize)
        plt.grid(True)
        plt.draw()
        # plt.show()
    else:
        plt.draw()


def animation_frame(i):
    compare_dayt_by_day(df, i)
    # compare_last_chapters(df, i)
    print(i)
    print("=============")
    return


def last_animation_frame(i):
    compare_last_chapters(df, i)
    print(i)
    print("=============")
    return


# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=2, metadata=dict(artist='Mayur Kanojiya'), bitrate=1800)


def get_last_animate():
    # return FuncAnimation(fig, func=last_animation_frame, frames=df[df['date'] > '17/08/20']['date'].unique())
    return FuncAnimation(fig, func=last_animation_frame, frames=['18/08/20','19/08/20','20/08/20','21/08/20'])

def get_animate():
    return FuncAnimation(fig, func=animation_frame, frames=df['date'].unique())

animate = get_last_animate()


animate.save('udacity_progress.mp4', writer=writer)



from datetime import datetime
PLOT_NUMBER = datetime.now().strftime('%d-%m-%Y')

PLOT_DIR = os.path.join(config.SCREENSHOT_DIR, 'plots')

FIG_NAME = os.path.join(PLOT_DIR, 'LAST-CHAPTER-' + str(PLOT_NUMBER) + '.png')

plt.show()
plt.clf()


df = df[df['date'] == '20/08/20']

df = df[df['lesson'].isin(['7-0','7-1','7-2','7-3''7-4','7-5','7-6','7-7','7-8','7-9', '8-0', '8-1'])].reset_index()

print(df.head())

sns.barplot(data=df
            , x='lesson'
            , y='views'
            , color='#02b3e4'
            , ci=None
            )
plt.title('Youtube Statistics | Microsoft Azure Machine Learning | Udacity')

plt.savefig(FIG_NAME, dpi=300, bbox_inches='tight')
plt.show()