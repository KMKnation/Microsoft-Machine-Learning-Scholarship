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

frame = len(df.values)

def animation_frame(i):
    compare_dayt_by_day(df, i)
    print(i)
    print("=============")
    return

# print(df[df['date'] == str('16/08/20')]['lesson'].values)

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=2, metadata=dict(artist='Mayur Kanojiya'), bitrate=1800)

animate = FuncAnimation(fig, func=animation_frame, frames=df['date'].unique())
animate.save('udacity_progress.mp4', writer=writer)

# plt.show()
