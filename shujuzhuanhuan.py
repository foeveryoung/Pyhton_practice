# -*- coding: utf-8 -*-
#C:/Users/Administrator/Desktop/
#http://mp.weixin.qq.com/s/vGxMuae-V2FouUW1exnTrw
#标准化
#1、零均值单位方差
from sklearn import preprocessing
import numpy as np
X = np.array([[1., -1., 2.], [2., 0., 0.], [0., 1., -1.]])
X_scaled = preprocessing.scale(X)
#scaled之后的数据零均值，单位方差
X_scaled.mean(axis=0)  # column mean: array([ 0.,  0.,  0.])
X_scaled.std(axis=0)  #column standard deviation: array([ 1.,  1.,  1.])
#2、StandardScaler----计算训练集的平均值和标准差，以便测试数据集使用相同的变换
scaler=preprocessing.StandardScaler().fit(X)
scaler.mean_
scaler.std_
#测试将该scaler用于输入数据，变换之后得到的结果同上
scaler.transform(X)

#归一化
# 1、MinMaxScaler(最小最大值标准化)公式：X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0)) ;
#　　　　X_scaler = X_std/ (max - min) + min
#例子：将数据缩放至[0, 1]间
X_train = np.array([[1., -1., 2.], [2., 0., 0.], [0., 1., -1.]])
min_max_scaler=preprocessing.MinMaxScaler()
X_train_minmax=min_max_scaler.fit_transform(X_train)
#将上述得到的scale参数应用至测试数据
X_test = np.array([[ -3., -1., 4.]])
X_test_minmax=min_max_scaler.transform(X_test)
min_max_scaler.scale_
min_max_scaler.min_

#2、MaxAbsScaler（绝对值最大标准化）
#与上述标准化方法相似，但是它通过除以最大值将训练集缩放至[-1,1]。这意味着数据已经以０为中心或者是含有非常非常多０的稀疏数据
X_train = np.array([[ 1., -1.,  2.],
                     [ 2.,  0.,  0.],
                    [ 0.,  1., -1.]])
max_abs_scaler = preprocessing.MaxAbsScaler()
X_train_maxabs = max_abs_scaler.fit_transform(X_train)
X_test = np.array([[ -3., -1.,  4.]])
X_test_maxabs = max_abs_scaler.transform(X_test)
max_abs_scaler.scale_

#3 对稀疏数据进行标准化


#二值化
X = [[ 1., -1.,  2.],
         [ 2.,  0.,  0.],
         [ 0.,  1., -1.]]
#binary
binarizer = preprocessing.Binarizer().fit(X)  # fit does nothing binarizer
#transform
binarizer.transform(X)
# 调整阈值
binarizer = preprocessing.Binarizer(threshold=1.1)
binarizer.transform(X)

#对特征类进行编码
enc = preprocessing.OneHotEncoder()
enc.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])
#transform
enc.transform([[0, 1, 3]]).toarray()

#缺失值的插补
import numpy as np
from sklearn.preprocessing import Imputer
#用均值插补缺失值
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit([[1, 2], [np.nan, 3], [7, 6]])
X = [[np.nan, 2], [6, np.nan], [7, 6]]
print(imp.transform(X))
#对稀疏矩阵进行缺失值插补
import scipy.sparse as sp
X = sp.csc_matrix([[1, 2], [0, 3], [7, 6]])
imp = Imputer(missing_values=0, strategy='mean', axis=0)
imp.fit(X)
X_test = sp.csc_matrix([[0, 2], [6, 0], [7, 6]])
print(imp.transform(X_test))

#七）生成多项式特征
#八）自定义转换