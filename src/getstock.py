import yfinance as yf
import os
import datetime as dt

#start = dt.datetime(2023,1,1)
start = dt.datetime(2020,1,1)
end = dt.datetime(2023,12,31)
df = yf.download('^HSI',start,end)

df.to_csv('data/HSI.csv')