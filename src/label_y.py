import numpy as np
import pandas as pd
import matplotlib.dates as mdates

data = pd.read_csv('data/HSIWithIndicator.csv')

# Mark 1 if increase: The closing price five trading days later is higher than today’s closing price
# Mark 0 if fall: The closing price five trading days later is lower than today’s closing price
data['week_trend'] = np.where(data.close.shift(-5) > data.close, 1, 0)
data.date = mdates.datestr2num(data.date)

data.to_csv('data/HSILabel.csv')