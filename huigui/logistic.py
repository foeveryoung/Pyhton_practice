# -*- coding: utf-8 -*-
#http://mp.weixin.qq.com/s/WH5SRwNPgVsNKW8xPiaEZA
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from ggplot import *
from scipy import stats
stats.chisqprob = lambda chisq, df: stats.chi2.sf(chisq, df)   #chisqprob is deprecated  and replace it with stats.distributions.chi2.sf


#读取数据集
purchase=pd.read_csv('C:/Users/Administrator/Desktop/Social_Network_Ads.csv')
#查看数据类型
print(purchase.dtypes)
#查看各变量缺失情况
purchase.isnull().sum()

#对性别做哑变量处理
dummy=pd.get_dummies(purchase.Gender)
#为防止多重共线性，将female剔除
dummy_drop=dummy.drop('Female',axis=1)  #1表示列
#剔除用户ID和Gender变量
purchase=purchase.drop(['User ID','Gender'],axis=1)
#如果调用logit类，需要给原数据添加截距项
purchase['Intercept']=1
#哑变量和原始数据合并
model_data=pd.concat([dummy_drop,purchase],axis=1)

#将数据集分为训练集和测试集
X=model_data.drop('Purchased',axis=1)
y=model_data['Purchased']
#训练集与测试集的比例为75%和25%
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.75,random_state=0)

#根据训练集构建Logistic分类器
logistic=smf.Logit(y_train,X_train).fit()
print(logistic.summary())

#剔除不显著变量重新构造分类器
X2=X_train.drop('Male',axis=1)
logistic2=smf.Logit(y_train,X2).fit()
logistic2.summary()
print(logistic.aic)
print(logistic2.aic)  #模型aic下降，说明删除合理
np.exp(logistic2.params) #优势比：模型解释系数

#根据分类器，在测试集上预测概率
prob=logistic2.predict(exog=X_test.drop('Male',axis=1))
pred=np.where(prob>=0.5,1,0)

#根据预测值和实际值构建混淆矩阵
cm=metrics.confusion_matrix(y_test,pred,labels=[0,1])
cm
#计算模型的准确率
accurancy=cm.diagonal().sum()/cm.sum()
accurancy

#利用ROC曲线面积衡量模型的合理性
fpr,tpr,_=metrics.roc_curve(y_test,pred)
df=pd.DataFrame(dict(fpr=fpr,tpr=tpr))
#一般AUC>0.8模型就比较好了
ggplot(df,aes(x='fpr',y='tpr'))+geom_area(alpha=0.5,fill='steelblue')+\
    geom_line()+geom_abline(linetype='dashed',color='red')+\
labs(x='1-specificity',y='Sensitivity',title='ROC Curve AUC=%.3f' % metrics.auc(fpr,tpr))