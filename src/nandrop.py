import pandas as pd

data = pd.read_csv('data/HSIWithIndicator.csv')
# check 缺值
data.isnull().sum()
# del na
data = data.dropna()

data.to_csv('data/HSIDropNA.csv')