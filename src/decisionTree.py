import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import graphviz 
from sklearn.metrics import confusion_matrix
import os
os.environ['PATH'] += os.pathsep + 'C:\Program Files\Graphviz\bin'

train = pd.read_csv('data/HSITrain.csv')
test = pd.read_csv('data/HSITest.csv')

# 訓練樣本再分成目標序列 y 以及因子矩陣 X
train_X = train.drop('week_trend', axis = 1)
train_y = train.week_trend
# 測試樣本再分成目標序列 y 以及因子矩陣 X
test_X = test.drop('week_trend', axis = 1)
test_y = test.week_trend

# 叫出一棵決策樹
model = DecisionTreeClassifier(max_depth = 7)

# 讓 A.I. 學習
model.fit(train_X, train_y)

# 讓 A.I. 測驗，prediction 存放了 A.I. 根據測試集做出的預測
prediction = model.predict(test_X)

dot_data = export_graphviz(model, out_file = None,
                           feature_names = train_X.columns,
                           filled = True, rounded = True,
                           class_names = True,
                           special_characters = True)
graph = graphviz.Source(dot_data)
graph

# 混淆矩陣
print(confusion_matrix(test_y, prediction))

# 準確率
print(model.score(test_X, test_y))