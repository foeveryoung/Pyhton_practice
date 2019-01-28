import newspaper
#coding=utf-8
from newspaper import Article
import urllib.request
import re
import datetime
import time
import os
import pandas as pd
# from fenci import readfile
# import csv
from bs4 import BeautifulSoup


def getcontent(link,date,date2,i,timess):
    try:
        req=urllib.request.Request(link)
        response=urllib.request.urlopen(req)
        html=response.read()
        soup=BeautifulSoup(html,"lxml")
        newscontent=soup.find('div',id='artibody')
        con=newscontent.find_all("p")
        content="。"
        for c in con:
            content=content+c.text
        title=soup.find('h1',id='artibodyTitle')
        #print(content)
        #print(title.text)
        timenews=time.strptime(timess, fmt)
        if (len(content) > 0):  # 判断文本是否识别
            content = content.replace("新浪声明：新浪网登载此文出于传递更多信息之目的，并不意味着赞同其观点或证实其描述。文章内容仅供参考，不构成投资建议。投资者据此操作，风险自担。",
                                          "")
            content = content.replace("进入【新浪财经股吧】讨论", "")
            # content.replace("\n","")
            # content.replace("[a-zA-Z]*","")
            # content.replace("\d*","")
            # content.replace(" ", "")
            if timenews<time15:
                pat = "D:/mathwork/python/new/train/news3/" + str(date2) + "/" + date + "_" + str(i) + ".txt"  # str(i)
                with open(pat, "w+", encoding="utf-8") as f:
                    f.write(content)
            else:
                date5 = date2+ datetime.timedelta(days=1)
                while str(date5) not in sday:
                    date5 = date5 + datetime.timedelta(days=1)
                pat = "D:/mathwork/python/new/train/news3/" + str(date5) + "/" + date + "_" + str(i) + ".txt"  # str(i)
                with open(pat, "w+", encoding="utf-8") as f:
                    f.write(content)
    except Exception as e:
        print("exception:"+str(e))
        time.sleep(1)

#获取每个页面中所有的子连接新闻
def getlink(url):
    try:
        data = urllib.request.urlopen(url).read()
        soup0 = BeautifulSoup(data, "lxml").find('div', class_="listBlk")
        link = []
        timesource = []
        source = soup0.find_all('li')
        for li in source:
            mm = li.find("a", attrs={'target': '_blank'}).get('href')
            if len(li.contents) == 2:
                link.append([mm, str(li.contents[1])[14:19]])  #当年时间没有年份，需要注意
            else:
                link.append([mm, "14:00"])
            # timesource.append(str(li.contents[1])[19:24])
        A = soup0.find('span', class_='pagebox_num')
        # for lin in soup0.find_all("a",attrs={'target':'_blank'}):
        #     link.append(lin.get('href'))
        # #print(link)
        if A is not None:
            pat = url.replace(".shtml", "")
            pageurl = pat + "_2.shtml"
            data2 = urllib.request.urlopen(pageurl).read()
            soup1 = BeautifulSoup(data2, "lxml").find('div', class_="listBlk")
            source1 = soup1.find_all('li')
            for li in source1:
                mm = li.find("a", attrs={'target': '_blank'}).get('href')
                if len(li.contents) == 2 :
                    link.append([mm, str(li.contents[1])[14:19]])
                else:
                    link.append([mm, "14:00"])
                # timesource.append(str(li.contents[1])[19:24])
                # for lin in soup1.find_all("a",attrs={'target':'_blank'}):
                #     link.append(lin.get('href'))
                # print("第二页")
        #print(len(link))
        # pat='http://finance.sina.com.cn/stock/marketresearch/.*\.shtml'
        # pat = 'https?://finance.sina.com.cn/stock/marketresearch/.*?\.shtml|https?://finance.sina.com.cn/roll/.*?\.shtml'
        # link=re.compile(pat).findall(data)
        # link=list(set(link))
        return link
    except Exception as e:
        print("exception:"+str(e))
        time.sleep(1)

#判断是否是节假日
def newdir(date):
    date2=str(date)
    print(date2)
    if date2 in sday:
        #print("zai")
        return  date            #返回文本形式
    else:
        date3=date
        while str(date3) not in sday:
            date3 = date3 + datetime.timedelta(days=1)
            #print(date3)
        return date3
#获取每一天新闻的链接
def geturl(start,end):
    for i in range((end - start).days + 1):
        date = start + datetime.timedelta(days=i)  # 新闻日期
        date2 = newdir(date)  # 交易日期
        urls = [None, None]
        urls[0] = "http://roll.finance.sina.com.cn/finance/zq1/gsjsy/" + str(date) + ".shtml"
        urls[1] = "http://roll.finance.sina.com.cn/finance/zq1/scyj/" + str(date) + ".shtml"
        # print(url)http://roll.finance.sina.com.cn/finance/zq1/scyj/2015-06-01.shtml
        # http://roll.finance.sina.com.cn/finance/zq1/gsjsy/2017-11-13.shtml
        num = 1
        for url in urls:
            try:
                linktime = getlink(url)
                # dpath = 'D:/mathwork/python/new/train/newspaper/' + date2  # 创建以日期命名的文件夹
                # if not os.path.exists(dpath):
                #     os.makedirs(dpath)
                for link in linktime:
                    getcontent(link[0], str(date), date2, num, link[1])
                    print("完成" + str(num) + "篇" + '\n')
                    num += 1
            except Exception as e:
                print("exception:" + str(e))
                time.sleep(1)



stockday=pd.read_csv("D:/mathwork/python/new/train/stockday3.csv",encoding="GBK").time #需要将csv文件日期格式设置为yyyy—mm-dd
sday=[None]*len(stockday)
for i in range(0,len(stockday)):
    sday[i]=str(stockday[i])
    #print(sday[i])
fmt = '%H:%M'
time15=time.strptime("15:00", fmt)
start=datetime.date(2018,1,3)
end=datetime.date(2018,4,17)   #为简便计算，最后的五个日期均为交易日
geturl(start,end)

# #分词
# files = os.listdir('D:/mathwork/python/new/train/newspaper')
# #print(files)
# with open("D:/mathwork/python/new/train/score.csv","w+") as csvf:
#     cname = ["date", "pos", "neg","twords"]
#     f=csv.writer(csvf)
#     f.writerow(cname)
#     alldata=[None]*len(files)          #用以储存每一次计算结果
#     m=0
#     for file in files:
#         pn=readfile('D:/mathwork/python/new/train/newspaper/'+file,str(file))  #文件名为日期
#         alldata[m]=pn
#         m=m+1
#     f.writerows(alldata)
