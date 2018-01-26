# -*- coding: utf-8 -*-
import pandas as pd
df=pd.read_csv('C:/Users/Administrator/Desktop/pollution_us_2000_2016.csv')
df.head()
#删除无意义的列
del df['Unnamed: 0']
df.head()
#字段信息
df.info()
#去除有缺失值记录
df.isnull().any()
df=df.dropna()
#新数据写入csv
df.to_csv('C:/Users/Administrator/Desktop/pollution_new.csv')
df=pd.read_csv('C:/Users/Administrator/Desktop/pollution_new.csv')

df=pd.read_csv('C:/Users/Administrator/Desktop/pollution_new.csv')
df[df['County']=='Queens']

#转化成pandas中的时间格式
from datetime import datetime
df['Date Local']=pd.to_datetime(df['Date Local'])
df.info()
df_Queens=df[df['County']=='Queens']
df_Queens_2000=df_Queens[df['Date Local'].dt.year==2000]
#每个月平均值，groupby聚合
df_Queens_2000['NO2 Mean'].groupby(df_Queens_2000['Date Local'].dt.month).mean()

#利用map函数对pandas的AQI列分等级
df_Queens['AQI']=df_Queens[['NO2 AQI','O3 AQI','SO2 AQI','CO AQI']].apply(lambda x:max(x),axis=1)  #列，左右之间取最大
def AQi_level(e):
    if e<=50:
        return 'Good'
    elif e>50 and e<=100:
        return 'Moderate'
    elif e>100 and e<=150:
        return 'Unhealthy for Sensitive Groups'
    elif e>150 and e<=200:
        return 'Unhealthy'
    elif e>200 and e<=300:
        return 'Very Unhealthy'
    else:
        return 'Hazardous'
df_Queens['AQI_level']=df_Queens['AQI'].map(AQi_level)
df_Queens['AQI_level'].value_counts()
df_Queens['AQI'].plot(kind='hist',figsize=[5,5],legend=False, title='AQI 2000-2016')
#饼图
df_Queens['AQI'].value_counts().plot(kind='pie',figsize=[5,5],legend=False, title='AQI 2000-2016')
