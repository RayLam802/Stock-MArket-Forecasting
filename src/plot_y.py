import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import pandas as pd
import numpy as np

data = pd.read_csv('data/HSIWithIndicator.csv')
df = data.copy()
df['week_trend'] = np.where(df.close.shift(-5) > df.close, 1, 0)

y = np.array(df.close[:-1])
#t = [dt.datetime.strptime(d,'%Y-%m-%d') for d in df.date[:-1]]
t = mdates.datestr2num(df.date[:-1])

fig, ax = plt.subplots() 
ax.plot_date(t, y, 'b-', color = 'black')
plt.show()

for i in range(len(df)):
    if df.week_trend[i] == 1:
        ax.axvspan(
            mdates.datestr2num(df.date[i]) - 0.5,
            mdates.datestr2num(df.date[i]) + 0.5,
            facecolor = 'red', edgecolor = 'none', alpha = 0.5
            )
    else:
        ax.axvspan(
            mdates.datestr2num(df.date[i]) - 0.5,
            mdates.datestr2num(df.date[i]) + 0.5,
            facecolor = 'green', edgecolor = 'none', alpha = 0.5
            )
fig.autofmt_xdate()
fig.set_size_inches(20, 10.5)
fig.savefig('define_y_3years.png')