import requests           #lxml是Python语言中处理XML和HTML功能最丰富，最易于使用的库
from lxml import etree

urls=['http://www.jianshu.com/users/54b5900965ea/followers?page={}'.format(str(i)) for i in range(1,6)]
print(urls)
for url in urls:
    print('11')
    html=requests.get(url)
    selector=etree.HTML(html.text)
    infos=selector.xpath('//ul[@class="user-list"]/li')
    if len(infos)>0:
        for info in infos:
            id=info.xpath('div/a/text()')[0]
            topic=info.xpath('div/div[1]/span[1]/text()')[0].strip('关注 ')
            fans=info.xpath('div/div[1]/span[2]/text()')[0].strip('粉丝 ')
            article=info.xpath('div/div[1]/span[3]/text()')[0].strip('文章 ')
            content={
                'id':id,
                'topic':topic,
                'fans':fans,
                'article':article
            }
            print(content)
            #xiangyou.insert_one(content)
    else:
        break
