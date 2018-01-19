# -*- coding: utf-8 -*-
#MLP多层感知器，一种简单的人工神经算法
# 在应用方面，MLP算法有一下优势：
#
# 1 能够构建非线性的模型
# 2 能够实现实时学习
#
# 当然也有其不足之处
# 1 损失函数非凸，局部最优解可能不止一个，所以初始权重如果随机设置的话，常常会导致交叉验证时得到的准确率数据无法对比。
# 2 存在相当数量的超参数需要进行调参
# 3 对特征缩放（feature scaling）敏感
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
data=pd.read_csv("C:/Users/Administrator/Desktop/BreastCancer_data.csv")
predi_features=data.iloc[:,2:32]
diagnosis=data.diagnosis
clf=MLPClassifier(activation="relu",batch_size=80,hidden_layer_sizes=(30,30),max_iter=200,random_state=42,learning_rate_init=0.001)
print(cross_val_score(cv=2,estimator=clf,n_jobs=-1,X=predi_features,y=diagnosis,scoring="accuracy"))


# hidden_layer_sizes
# 隐藏层层数和每层神经元个数设置，默认值为（100，),设置为（5，3）表示有两层隐藏层，一个隐藏层有5个神经元，第二个隐藏层3个神经元
#
# activation
# 有四种激活函数可以选择{‘identity’, ‘logistic’, ‘tanh’, ‘relu’},，默认是relu激活函数，一般都使用relu ，四种激活函数的形式如下：
# ‘identity’,  f(x) = x
# ‘logistic’,  f(x) = 1 / (1 + exp(-x)).
# ‘tanh’,  f(x) = tanh(x).
# ‘relu’,  f(x) = max(0, x)
#
# solver
# solver是通过不断寻找损失函数最优解来进行权重迭代更新的优化器，有三种可以选择 {‘lbfgs’, ‘sgd’, ‘adam’}，默认设置是“adam”，‘lbfgs’ 是拟牛顿法的一种，.‘sgd’ 是随机梯度下降法，‘adam’ 是基于随机梯度下降的另一种优化算法，adam在大规模训练集上表现优秀（相对来说能够节省训练时间和提高validation score），lbfgs在小规模训练集上效果更好，收敛更快。
#
# alpha
# 正则化参数. alpha是进行L2惩罚项的参数。默认值为0.0001
#
# batch_size
# 批尺寸，一般对随机优化方法都需要批尺寸这个参数，默认为min(200, n_samples)，即200和训练集样本量两者之间的最小值，当然如果solver选择了lbfgs的话，就没有必要使用批尺寸了。
# learning_rate
# 中文翻译为学习率，各种教程里面经常用或者表示，有三个选项可供选择 {‘constant’, ‘invscaling’, ‘adaptive’}，‘constant’ 表示设置学习率为常数，全程不变，‘invscaling’ 则会逐渐减小学习率，减小的方法是effective_learning_rate = 初始学习率 / pow(t, power_t)，  power_t的默认值是0.5. 相当于迭代一个step，把steps开方得到一个值factor，然后让初始学习率除以这个factor，这样就持续降级学习率，梯度下降的步子越来越小，避免震荡。
#
# ‘adaptive’会依据损失函数的值来调整学习率，只要训练时的损失函数值一直下降，学习率不变。但是如果连续两次迭代都没有降低损失函数一个tol的值，或者将validation score提高一个tol，在early_stopping参数为on的情况下，当前的学习率会除以五，‘adaptive’只在solver选择sgd的时候有效。
#
# learning_rate_init
# 学习率初始值设置为0.001，该设置只有在solver为sgd或者adam时候才有效。
#
# power_t
# 设置指数，用来控制学习率降低的速度，学习率那里如果选择了 ‘invscaling’时可以设置这个参数，该参数只对sgd有效。
#
# max_iter
# 最大迭代次数，默认值是200，对于随机优化器来说(sgd和adam), 如果迭代过程中出现了tol定义的收敛或者是到达最大迭代次数，训练就会停止。注意这个参数控制的是epoch，而不是steps。关于epoch和steps的区别，在stackoverflow上面有很好的解释，链接点这里：https://stackoverflow.com/questions/4752626/epoch-vs-iteration-when-training-neural-networks
#
# shuffle
# 每次迭代之前是否先对数据随机排列下顺序（洗牌），只对随机优化器有效，默认值为True.
#
# random_state
# 是否设置随机种子，默认值为None。
#
# tol
# 优化阈值，默认值为0.0001，连续两次迭代如果损失函数的值没有降低一个tol或者分数没有提高一个tol，就认为已经收敛，训练进程就会停止，除非学习率设置为adaptive。
#
# verbose
# 默认值为False，是否打印迭代的输出。
#
# warm_start
# 默认值是False，如果设置为True，就重复利用上次fit的结果作为初始值，这样可以提高神经网络训练结果的利用率。
#
# early_stopping
# 该参数的作用是当validation score没有改善时，是否要终止训练。如果把early_stopping设置为True，神经网络在训练的时候会自动拿出10%的训练数据出来作为validation数据集，如果连续两次迭代validation score都没有提高一个tol，训练过程就会中止。该参数只有在使用随机优化器（sgd，adam）的时候有效。默认值为False。
#
# validation_fraction
# validation比例，如果前面的early_stopping设置为True，这个参数取值为0到1之间，设置拿出多少比例的训练集数据做validation，默认值为0.1。
#
# momentum ，nesterovs_momentum ，beta_1 ，beta_2 ，epsilon 这些变量都是控制梯度下降的幅度或方向的参数，尤其是使用adam这个优化器时。一般可采取默认值，如果想了解这几个参数的具体含义，可以参考Hands-On Machine Learning with Scikit Learn and TensorFlow 这本书的第十一章。