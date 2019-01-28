#coding=utf-8
import jieba
import numpy as np
import re
import os
import csv


#打开词典
def open_dic(Dict,path):
    dictionary=open(path,"r",encoding="GBK")
    dict=[]
    for word in dictionary:
        word=word.strip("\n")
        word = word.lstrip()
        word = word.rstrip()
        dict.append(word)
    return dict


def judgeodd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
posdict=open_dic("positive","D:/mathwork/python/new/train/newpos.txt")
negdict=open_dic("negative","D:/mathwork/python/new/train/newneg.txt")
jieba.load_userdict("D:/mathwork/python/new/train/newneg1.txt")  #读取文件前先要将文件转化为utf-8格式
jieba.load_userdict("D:/mathwork/python/new/train/newpos1.txt")

#每篇新闻的词汇得分
def sentiment_score_list(data):
    data=re.sub("[a-zA-Z0-9\s+\.\!_,$%^*()?;；:-【】+\"\'+——！，。;：:？、~@#￥■%……&*（）]+", "/", data)
    seg_sentence=data.split("/") #分词
    #print(seg_sentence)
    countall=0
    poscount = 0
    negcount = 0
    for sen in seg_sentence:
        segtmp=jieba.cut(sen)#分词。以列表形式展示
        for word in segtmp:
            countall+=1
            if word in posdict:
                poscount+=1
                #print("************")
            elif word in negdict:
                negcount+=1
                #print("+++++++++++")
    return [poscount,negcount,countall]

def sentiment_score(senti_score_list):
    score_array=np.array(senti_score_list[0])
    Pos=float(np.sum(score_array[:,0])/senti_score_list[1])
    Neg=float(np.sum(score_array[:,1])/senti_score_list[1])
    print("Positive : "+str(Pos))
    print("Negative : " + str(Neg))

#读取文件中新闻
def readfile(path,date):
    files=os.listdir(path)
    numfiles=len(files)
    print(files)
    tpos=0  #每日积极总词汇
    tneg=0
    twords=0
    for file in files:
        data=open(path+"/"+file,encoding='utf-8').read()
        wscore=sentiment_score_list(data)
        tpos+=wscore[0]
        tneg+=wscore[1]
        twords+=wscore[2]
    #Pos=float(tpos/twords)
    #Neg=float(tneg/twords)
    return [date,tpos,tneg,twords,numfiles]

#逐行写入CSV文件
# files = os.listdir('D:/mathwork/python/new/train/news/')
# #print(files)
# with open("F:/python/scorenew11.csv","w+") as csvf:
#     cname = ["date", "pos", "neg","twords"]
#     f=csv.writer(csvf)
#     f.writerow(cname)
#     alldata=[None]*len(files)          #用以储存每一次计算结果
#     m=0
#     for file in files:
#         pn=readfile('D:/mathwork/python/new/train/news/'+file,str(file))  #文件名为日期
#         alldata[m]=pn
#         m=m+1
#     f.writerows(alldata)

files2 = os.listdir('F:/python/news/')
#print(files)
with open("F:/python/scorenewnewnew.csv","w+") as csvf2:
    cname2 = ["date", "pos", "neg","twords","numfiles"]
    f2=csv.writer(csvf2)
    f2.writerow(cname2)
    alldata2=[None]*len(files2)          #用以储存每一次计算结果
    m=0
    for file in files2:
        pn2=readfile('F:/python/news/'+file,str(file))  #文件名为日期
        alldata2[m]=pn2
        m=m+1
    f2.writerows(alldata2)

#print(files)

#print(readfile('D:/mathwork/python/new/train/newspaper/2015-06-01'))
#http://www.cnblogs.com/zhzhang/p/6785125.html
