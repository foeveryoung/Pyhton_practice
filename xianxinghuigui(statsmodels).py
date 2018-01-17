import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

#读取数据
sales=pd.read_csv('C:/Users/Administrator/Desktop/Advertising.csv')
sales.head()  #查看前五行
#print(sales.describe()) #查看描述性统计

#抽样构造训练集和测试集
Train,Test=train_test_split(sales,train_size=0.8,random_state=1234)

#建模
fit=smf.ols('sales~TV+radio+newspaper',data=Train).fit()
#模型概览的反馈
print(fit.summary())

fit2=smf.ols('sales~TV+radio',data=Train.drop('newspaper',axis=1)).fit()
#print(fit2.summary())

#第一个模型的测试结果
pred=fit.predict(exog=Test)
#第2个模型的测试结果
pred2=fit2.predict(exog=Test.drop('newspaper',axis=1))

#模型效果比对
RMSE=np.sqrt(mean_squared_error(Test.sales,pred))
RMSE2=np.sqrt(mean_squared_error(Test.sales,pred2))

print('第一个模型的预测效果：RMSE=%.4f\n' %RMSE)
print('第而个模型的预测效果：RMSE=%.4f\n' %RMSE2)

#真实值与预测值之间的关系 #设置绘图风格
plt.style.use('ggplot')
#设置中文编码和负号的正常显示
plt.rcParams['font.sans-serif']='Microsoft Yahei'

#散点图
plt.scatter(Test.sales,pred,label='观测点')
plt.plot([Test.sales.min(),Test.sales.max()],[pred.min(),pred.max()],'r-',lw=2,label='拟合线')

#添加轴标签和标题
plt.title('真实值VS预测值')
plt.xlabel('真实值')
plt.ylabel('预测值')

#去除图边框的顶部刻度和右边刻度
plt.tick_params(top='off',right='off')
#添加图例
plt.legend(loc='upper left')
#图形展现
plt.show()
