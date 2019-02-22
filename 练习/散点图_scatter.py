import pandas as pd
import matplotlib.pyplot as plt


# # 设置绘图风格
# plt.style.use('ggplot')
# # 设置中文编码和负号的正常显示
# plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
# plt.rcParams['axes.unicode_minus'] = False
# cars=pd.read_csv('C:/Users/Administrator/Desktop/cars.csv')
# plt.scatter(cars.speed, # x轴数据为汽车速度
#             cars.dist, # y轴数据为汽车的刹车距离
#             s = 30, # 设置点的大小
#             c = 'steelblue', # 设置点的颜色
#             marker = 's', # 设置点的形状
#             alpha = 0.9, # 设置点的透明度
#             linewidths = 0.3, # 设置散点边界的粗细
#             edgecolors = 'red' # 设置散点边界的颜色
#             )
# # 添加轴标签和标题plt.title('汽车速度与刹车距离的关系')
# plt.xlabel('汽车速度')
# plt.ylabel('刹车距离')
# # 去除图边框的顶部刻度和右边刻度
# plt.tick_params(top = 'off', right = 'off')
# # 显示图形
# plt.show()


# # 花瓣数据
# iris = pd.read_csv('iris.csv')
# # 自定义颜色
# colors = ['steelblue', '#9999ff', '#ff9999']
# # 三种不同的花品种S
# pecies = iris.Species.unique()
# # 通过循环的方式，完成分组散点图的绘制
# for i in range(len(Species)):
#     plt.scatter(iris.loc[iris.Species == Species[i], 'Petal.Length'],
#                 iris.loc[iris.Species == Species[i], 'Petal.Width'],
#                 s = 35, c = colors[i], label = Species[i])
# # 添加轴标签和标题
# plt.title('花瓣长度与宽度的关系')
# plt.xlabel('花瓣长度')
# plt.ylabel('花瓣宽度')
# # 去除图边框的顶部刻度和右边刻度
# plt.tick_params(top = 'off', right = 'off')
# # 添加图例
# plt.legend(loc = 'upper left')
# # 显示图形
# plt.show()

# 气泡图绘制
# 导入第三方包
# import numpy as np
# # 读取数据
# sales = pd.read_excel('sales.xlsx')
# # 绘制气泡图
# plt.scatter(sales.finish_ratio,
#             sales.profit_ratio,
#             c = 'steelblue',
#             s = sales.tot_target/30,
#             edgecolor = 'black')
#
# # 改变轴刻度的显示方式（百分比形式）
# plt.xticks(np.arange(0,1,0.1), [str(i*100)+'%' for i in np.arange(0,1,0.1)])
# plt.yticks(np.arange(0,1,0.1), [str(i*100)+'%' for i in np.arange(0,1,0.1)])
# # 设置x轴和y轴的数值范围
# plt.xlim(0.2, 0.7)
# plt.ylim(0.25, 0.85)
# # 添加轴标签和标题
# plt.title('完成率与利润率的关系')
# plt.xlabel('完成率')
# plt.ylabel('利润率')
# # 去除图边框的顶部刻度和右边刻度
# plt.tick_params(top = 'off', right = 'off')
# # 显示图形
# plt.show()
