import requests
import re
from datetime import datetime
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import config
import os

with open('resource/udacity_azure.json', 'r') as cfile:
    content = json.load(cfile)


def getStats(link):
    page = requests.get(link)
    print(page.text)
    # <meta itemprop="interactionCount" content="1488">
    views = re.search('"interactionCount" content=(\d*.\d*.\d*)', page.text).group(1).replace('"', '')
    title = re.search("property=\"og:title\" content=\"([^\n]*)", page.text).group(1)
    return (views, title)


def get_youtube_url(id):
    return "https://www.youtube.com/watch?v={}".format(id)


lessons = []
views = []
names = []
for lesson in content:
    index = str(lesson['index'])
    chapters = lesson['chapters']
    for i in range(len(chapters)):
        index += '.' + str(i)
        name = chapters[i]['name']
        URL = get_youtube_url(chapters[i]['youtube'])
        # (view_count, title) = getStats(URL)

        lessons.append(index)
        index = str(lesson['index'])
        views.append(int(0))
        names.append(name)

udacity_stats = {
    "date": datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
    'lesson': lessons,
    'views': views,
    'name': names
}

print(udacity_stats)
df = pd.DataFrame(udacity_stats)

sns.barplot(data=df
            , x='lesson'
            , y='views'
            , color='#02b3e4'
            , ci=None
            )

plt.show()

if os.path.exists(config.DATA_FILE):
    df.to_csv(config.DATA_FILE, mode='a', header=False, index=False)
else:
    df.to_csv(config.DATA_FILE, index=False)
