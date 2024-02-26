import pandas as pd

data = pd.read_csv('data/HSILabel.csv')

# 決定切割比例為 70%:30%
split_point = int(len(data)*0.7)
# 切割成學習樣本以及測試樣本
train = data.iloc[:split_point,:].copy()
test = data.iloc[split_point:-5,:].copy()

train.to_csv('data/HSITrain.csv')
test.to_csv('data/HSITest.csv')