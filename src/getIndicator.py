import pandas as pd
from stockstats import wrap

data = pd.read_csv('data/HSI.csv')
df = wrap(data)
macd = df['macd']
rsi = df['rsi']
tema = df['tema']
adr = (df['high_-1_s'] - df['low_-1_s'] + df['high_-2_s'] - df['low_-2_s'] + df['high_-3_s'] - df['low_-3_s']
            + df['high_-4_s'] - df['low_-4_s'] + df['high_-5_s'] - df['low_-5_s']) / 5

data.loc[:, "MACD"] = macd
data.loc[:, "RSI"] = rsi
data.loc[:, "TEMA"] = tema
data.loc[:, "ADR"] = adr

outputDf = pd.DataFrame(data)

outputDf.to_csv('data/HSIWithIndicator.csv')