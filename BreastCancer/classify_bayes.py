import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score
nbClf=GaussianNB()
data=pd.read_csv("C:/Users/Administrator/Desktop/BreastCancer_data.csv")
predi_features=data.iloc[:,2:32]
diagnosis=data.diagnosis
print(cross_val_score(nbClf,X=predi_features,y=diagnosis,cv=5,scoring="accuracy"))