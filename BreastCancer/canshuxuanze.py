# -*- coding: utf-8 -*-
#C:/Users/Administrator/Desktop/
#http://mp.weixin.qq.com/s/UzWOGoJ3OLOT0KjeEMrv2g
ws_data=pd.read_csv("C:/Users/Administrator/Desktop/BreastCancer_data.csv")
diagnosis=ws_data.diagnosis
predi_features=ws_data.iloc[:,2:32]

#网格搜索
from sklearn.ensemble import RandomForestClassifier
##先建一个随机森林分类器
rfClf=RandomForestClassifier()
from sklearn.model_selection import GridSearchCV
##设置参数网格，随机森林默认的bootstrap是True，第一个网格只涉及两个参
##数：树的数量和特征变量个数，前者有三个值可以选择，后者有四个值可
##选，有12种组合，后面一个dict格式储存的是另一种网格，在bootstrap参数设
##置为False的情况下，树的数量有两个值可选，max_feature有三个值可选，
##共有6种组合，加上前面12种就是18种组合。
hypermeter_grid=[{'n_estimators':[3,10,15],
                'max_features':[2,4,6,8]},
                 {'bootstrap':[False],
                 'n_estimators':[3,10],
                 'max_features':[2,3,4]}]
##设置三折交叉验证，评价指标选F1
grid_search=GridSearchCV(rfClf,hypermeter_grid,cv=3,scoring="f1")
grid_search.fit(predi_features,diagnosis=="M")
grid_search.best_params_
grid_search.grid_scores_

#随机搜索的方法
## 调用scipy里的整数随机分布
from scipy.stats import randint as sp_randint
from sklearn.model_selection import RandomizedSearchCV
## 将max_features,min_samples_split,以及min_samples_leaf的随机分布设置
## 好，注意这里不能用np.random.randomint函数，这里要求的是分布不是抽样结果
random_grid={"max_depth": [3, None],
              "max_features": sp_randint(1, 20),
              "min_samples_split":sp_randint(2, 11),
              "min_samples_leaf": sp_randint(1, 11),
              "bootstrap": [True, False],
              "criterion": ["gini", "entropy"]}
## 随机抽取10次参数组合
n_iteration=10
## 设置三折交叉验证，评价分数为F1

random_grid_search=RandomizedSearchCV(cv=3,estimator=rfClf,n_iter=n_iteration,
                                      scoring='f1',param_distributions=random_grid)
## 拟合数据
random_grid_search.fit(predi_features,diagnosis=="M")
## 查看最佳F1得分
random_grid_search.best_score_
## 查看最佳参数组合
random_grid_search.best_params_
## 查看10次参数组合的得分情况
random_grid_search.grid_scores_