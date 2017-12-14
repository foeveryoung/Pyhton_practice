import urllib.request
from bs4 import BeautifulSoup
import pandas

url='https://www.qidian.com/rank/hotsales?page=1'
data=urllib.request.urlopen(url).read().decode('utf-8')
#print(data)
bookr=BeautifulSoup(data,'lxml')
article=[]
info={}
author=bookr.select('.author a') #选中author 下的a标签
name=bookr.select('.book-mid-info h4')
update=bookr.select('.update a')
for i in range(0,20):
    info['author']=(author[0+2*i].text)
    info['name']=(name[0+i].text)
    info['style']=(author[1+2*i].text)
    info['update']=(update[i].text)
    article.append(info)
    info={}
art=pandas.DataFrame(article)
print(art)


