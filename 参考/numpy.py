#数学领域的线性代数、傅里叶变换；统计学领域的统计计算、随机数生成
import numpy as np
#
# #s使用nump构建矩阵
# arr1=np.array([1,3,5,7,9])
# print(arr1)  #[1 3 5 7 9]
# arr2=np.array((10,20,30))
# print(arr2)   #[10 20 30]
# arr3=np.array([[1,2,3,4],[5,6,7,8],[3,4,6,8]])
# print(arr3)   #[[1 2 3 4]
#               # [5 6 7 8]
#               # [3 4 6 8]]
#
# #返回一个数组的行数和列数
# print(arr1.shape) #(5,)
# print(arr3.shape)  #(3, 4)
#
# #元素获取
# print(arr3,'\n') #输出后换行
# print(arr3[1,:],'\n')
# print(arr3[[0,2],:],'\n') #获取某几行
# print(arr3[[0,2],[2,3]],'\n') #获取索引位置元素  [3 8]
# print(arr3(np.ix_([0,2],[2,3])))  #返回由第一行、第三行、第三列和第四列组成的2×2矩阵
#
# 数学函数
# # 取绝对值
# np.abs
# np.fabs
#
# # 算术平方根
# np.sqrt
#
# # 平方
# np.square
#
# # 指数
# np.exp
#
# # 对数
# np.log2
# np.log10
# np.log(x,base)
#
# # 符号函数（大于0的数返回1、小于0的数返回-1、0返回0值）
# np.sign
#
# # 向上取整
# np.cell
#
# # 向下取整
# np.floor
#
# # 返回最近的整数
# np.rint
#
# # 判断是否缺失
# np.isnan
#
# # 判断是否有限
# np.isfinite
#
# # 判断是否无限
# np.isinf
#
# # 幂运算
# np.power
#
# # 余数
# np.mod
#
# 统计函数
#
# # 最大值
# np.max
#
# # 浮点型的最大值
# np.fmax
#
# # 最小值
# np.mim
#
# # 浮点型的最小值
# np.fmin
#
# # 求和
# np.sum
#
# # 均值
# np.mean
#
# # 标准差
# np.std
#
# # 方差
# np.var
#
# # 中位数
# np.median


#有时候为了使每次产生的随机数都相同，就需要设置固定的随机种子，设置随机种子
# 可以调用seed函数实现

#二项分布：在概率论和统计学中，二项分布是n个独立的是/非试验中成功的次
# 数的离散概率分布，其中每次试验的成功概率为p

np.random.seed(123)
r1=np.random.binomial(n=10,p=0.2,size=10)
print(r1,'\n')
r2=np.random.binomial(n=10,p=0.2,size=(3,5))
print(r2,'\n')
#泊松分布
r3=np.random.poisson(lam=6,size=10)
r4=np.random.poisson(lam=(10,50,20),size=(5,3))
#正态分布
np.random.seed(2)
r5=np.random.normal(loc=2,scale=3,size=10)#均值为2方差为3
#自由度为2的t分布
r7=np.random.standard_t(df=3,size=(2,3))
#自由度为2和5的t分布
r8=np.random.f(dfnum=3,dfen=5,size=(2,3))
#1到10之间的均匀分布,并四舍五入
r9=np.round(np.random.uniform(size=(3,4),low=1,high=10),0)

#numpy模块还提供了读取数据与写数据的函数，方便我们将外部数据文件读入到
# Python的工作环境中
data1=np.loadtxt(fname='ads.txt',delimiter=',',skiprows=1)
# data2=np.genfromtxt(fname='load.txt',delimiter=',',skip_header=1,usecols=[0,2])
# fname：指定外部文件的路径
# delimiter：指定文件中数据列的分隔符
# skiprows：指定读数时跳过的行数
# skip_header：指定跳过首行
# usecols：指定读取的数据列

#数据写出
np.savetxt(fname,X,fmt='%.18e',delimiter=' ',newline='\n',header='',footer='',comments='# ')
# fname：指定数据写出的路径
# X：指定需要写出的数据
# fmt：指定输出数据的格式，默认科学计算法
# delimiter：指定数据列之间的分隔符，默认空格符
# newline：指定新行的标识符，默认换行
# header：指定输出数据首行值
# footer：指定输出数据的末行值
# comments：指定注释符，默认“#”
