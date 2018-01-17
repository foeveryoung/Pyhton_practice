import pandas as pd
import numpy as np
from patsy import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm
import  scipy.stats as stats
from sklearn.metrics import mean_squared_error
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

ccpp=pd.read_excel('C:/Users/Administrator/Desktop/CCPP.xlsx')
#print(ccpp.describe())
#AT温度 V压力AP相对湿度 RH排气量 PE发电量
#绘制各变量之间的散点图
#sns.pairplot(ccpp)
#plt.show()

#发电量与自变量之间的相关系数
print(ccpp.corrwith(ccpp.PE))   #一般皮尔森系数低于0.4说明弱相关

#多重共线性检验
#若VIF大于10说明存在多重共线性
#将因变量PE，自变量AT，V，AP和截距项以数据框的形式组合起来
y,X=dmatrices('PE~AT+V+AP',data=ccpp,return_type='dataframe')
#构造空的数据框
vif=pd.DataFrame()
vif["VIF Factor"]=[variance_inflation_factor(X.values,i) for i in range(X.shape[1])]
vif["features"]=X.columns
print(vif)

#异常点检测
#检测之前需要构造线性模型
fit=sm.formula.ols('PE~AT+V+AP',data=ccpp).fit()
print(fit.summary())
#计算模型的RMSE
pred=fit.predict()
print(np.sqrt(mean_squared_error(ccpp.PE,pred)))
#关于异常点的检测方法，一般可以通过高杠杆值点（帽子矩阵
# ）或DFFITS值、学生化残差、cook距离和covratio值来判断
#离群点检验通过参考薛毅老师的《统计建模与R软件》书可知，当高杠杆值点（或帽子矩阵）
# 大于2(p+1)/n时，则认为该样本点可能存在异常（其中p为自变量的个数，n为观测的个数）；
# 当DFFITS统计值大于2sqrt((p+1)/n)时 ，则认为该样本点可能存在异常；当学生化残差的绝对
# 值大于2，则认为该样本点可能存在异常；对于cook距离来说，则没有明确的判断标准，一般来说，
# 值越大则为异常点的可能性就越高；对于covratio值来说，如果一个样本的covratio值离数值1越
# 远，则认为该样本越可能是异常值。这里我们就以学生化残差作为评判标准，因为其包含了帽子矩
# 阵和DFFITS的信息
outliers=fit.get_influence()
# 高杠杆值点（帽子矩阵）
leverage = outliers.hat_matrix_diag
# dffits值
dffits = outliers.dffits[0]
# 学生化残差
resid_stu = outliers.resid_studentized_external
# cook距离
cook = outliers.cooks_distance[0]
# covratio值
covratio = outliers.cov_ratio
# 将上面的几种异常值检验统计量与原始数据集合并
contat1 = pd.concat([pd.Series(leverage, name = 'leverage'),pd.Series(dffits, name = 'dffits'),
                     pd.Series(resid_stu,name = 'resid_stu'),pd.Series(cook, name = 'cook'),
                     pd.Series(covratio, name = 'covratio'),],axis = 1)
ccpp_outliers = pd.concat([ccpp,contat1], axis = 1)
ccpp_outliers.head()
# covratio值
# 计算异常值数量的比例
outliers_ratio = sum(np.where((np.abs(ccpp_outliers.resid_stu)>2),1,0))/ccpp_outliers.shape[0]
outliers_ratio
# 删除异常值
ccpp_outliers = ccpp_outliers.loc[np.abs(ccpp_outliers.resid_stu)<=2,]
# 重新建模
fit2 = sm.formula.ols('PE~AT+V+AP',data = ccpp_outliers).fit()
fit2.summary()
# 计算模型的RMSE值
pred2 = fit2.predict()
np.sqrt(mean_squared_error(ccpp_outliers.PE, pred2))

#正态性检验
#<><>><><><><><><><><><><><><><><><>
# 残差的正态性检验（直方图法）
resid = fit2.resid
# 中文和负号的正常显示
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
plt.hist(resid, # 绘图数据
        bins = 100, # 指定直方图条的个数
        normed = True, # 设置为频率直方图
        color = 'steelblue', # 指定填充色
        edgecolor = 'k') # 指定直方图的边界色

# 设置坐标轴标签和标题
plt.title('残差直方图')
plt.ylabel('密度值')
# 生成正态曲线的数据
x1 = np.linspace(resid.min(), resid.max(), 1000)
normal = mlab.normpdf(x1, resid.mean(), resid.std())
# 绘制正态分布曲线
plt.plot(x1,normal,'r-', linewidth = 2, label = '正态分布曲线')
# 生成核密度曲线的数据
kde = mlab.GaussianKDE(resid)
x2 = np.linspace(resid.min(), resid.max(), 1000)
# 绘制核密度曲线
plt.plot(x2,kde(x2),'k-', linewidth = 2, label = '核密度曲线')
# 去除图形顶部边界和右边界的刻度
plt.tick_params(top='off', right='off')
# 显示图例
plt.legend(loc='best')
# 显示图形
plt.show()
#<><>><><><><><><><><><><><><><><><>
# 残差的正态性检验（PP图和QQ图法）
pp_qq_plot = sm.ProbPlot(resid)
pp_qq_plot.ppplot(line = '45')
plt.title('P-P图')
pp_qq_plot.qqplot(line = 'q')
plt.title('Q-Q图')# 显示图形plt.show()
#<><><><><><><><><><><><><><><><><><>
# 残差的正态性检验（非参数法）
standard_resid = (resid-np.mean(resid))/np.std(resid)
stats.kstest(standard_resid, 'norm')

#如果残差不服从正态分布的话，建议对Y变量进行box-cox变换处理。
# 由于fit2模型的残差并没有特别明显的偏态（偏度为0.058，接近于0），
# 故这里就不对Y变量进行box-cox变换了。如果需要变换的话，可以以下面的代码为例：
# import scipy.stats as stats
# # 找到box-cox变换的lambda系数
# lamd = stats.boxcox_normmax(your_data_frame.y, method = 'mle')
# # 对Y进行变换
# # your_data_frame['trans_y'] = stats.boxcox(your_data_frame.y, lamd)
# #  建模
# fit = sm.formula.ols('y~x1+x2+...',
# data = your_data_frame).fit()
# fit.summary()