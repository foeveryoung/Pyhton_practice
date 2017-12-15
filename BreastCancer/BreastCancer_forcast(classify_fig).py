import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
ws_data=pd.read_csv("C:/Users/Administrator/Desktop/BreastCancer_data.csv")
diagnosis=ws_data.diagnosis
predi_features=ws_data.iloc[:,2:32]


class winsconBC:
    def __init__(self, data_y, method, rand_seed=42, Nfolds=3, shuffled=True):
        from sklearn.cross_validation import StratifiedKFold
        self.data = data_y
        self.clf = method
        self.Rseed = rand_seed
        self.Nfolds = Nfolds
        self.shuffle = shuffled
        self.classifier = method
        self.sfk = StratifiedKFold(y=self.data, n_folds=self.Nfolds, random_state=self.Rseed, shuffle=self.shuffle)

    def classify(self):
        accuracy = list()
        for TR, TS in self.sfk:
            train_x, train_y = predi_features.iloc[TR, :], diagnosis[TR]
            test_x, test_y = predi_features.iloc[TS, :], diagnosis[TS]
            if self.classifier == "logistic":
                from sklearn.linear_model import LogisticRegression
                logClf = LogisticRegression()
                logClf.fit(train_x, train_y)
                accuracy.append(logClf.score(X=test_x, y=test_y))

            if self.classifier == "SGD":
                from sklearn.linear_model import SGDClassifier
                SGDclf = SGDClassifier(loss="log", max_iter=1000,
                                       learning_rate="optimal")  ### 手动设置参数，详见sklearn官网
                SGDclf.fit(X=train_x, y=train_y)
                accuracy.append(SGDclf.score(X=test_x, y=test_y))

        if self.classifier == "SVM":
            from sklearn.svm import SVC
            svmClf = SVC(kernel="linear", C=1)  ### 这里设置kernal=linear,不再是默认的rbf
            svmClf.fit(X=train_x, y=train_y)
            accuracy.append(svmClf.score(X=test_x, y=test_y))

        if self.classifier == "randomforest":
            from sklearn.ensemble import RandomForestClassifier
            rfClf = RandomForestClassifier()
            rfClf.fit(train_x, train_y)
            accuracy.append(rfClf.score(test_x, test_y))

        return (np.array(accuracy))

whole=list()
for i in range(50): ### 重复两百次
    mean_acu_score=list()
    for s in ["SGD",'logistic','SVM',"randomforest"]:
        mean_acu_score.append(np.mean(winsconBC(
        data_y=diagnosis,method=s,rand_seed=i,
        Nfolds=5,shuffled=True).classify()))
    whole.append(mean_acu_score)
test_results=np.array(whole)###  我们把200次的对比数值可视化的方式展示出来

plt.figure(figsize=(10,5))
x=np.arange(1,51)
y_SGD=test_results[:,0]
y_logistic=test_results[:,1]
y_svm=test_results[:,2]
y_rf=test_results[:,3]

L1, =plt.plot(x,y_SGD,label="a")
L2, =plt.plot(x,y_logistic,c="r",label="b")
L3, =plt.plot(x,y_svm,c="y",label="c")
L4, =plt.plot(x,y_rf,c="b",label="d")
plt.legend(handles=[L1,L2,L3,L4],labels=["SGD",'logistic','SVM',"randomforest"],loc="best")
plt.show()
