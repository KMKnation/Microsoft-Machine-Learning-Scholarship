from datetime import datetime
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

with open('resource/udacity_azure.json', 'r') as cfile:
    content = json.load(cfile)

udacity_stats = {
    "date": datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
    'lessons': [1.1, 1.2, 1.3],
    'views': [8000, 200, 300]
}

print(udacity_stats)
df = pd.DataFrame(udacity_stats)
print(df.head())

sns.barplot(data=df
            , x='lessons'
            , y='views'
            , color='#02b3e4'
            , ci=None
            )

plt.show()