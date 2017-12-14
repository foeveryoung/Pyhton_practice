import time
# for i in range(0,10):
#     print(i)
#     time.sleep(1)

#print(time.time())#从1970年1月1日物业计算，至今为止经过了多长时间，以秒为单位计算

#print(time.localtime()) #给出当下时间，细致到秒
#time.struct_time(tm_year=2017, tm_mon=11, tm_mday=28, tm_hour=22, tm_min=20, tm_sec=38, tm_wday=1, tm_yday=332, tm_isdst=0)

#print(time.mktime(time.localtime())) #将本地时间转化为时间戳时间

#print(time.asctime(time.localtime())) #巴表示时间的元组或者时间structur表示成Tue Nov 28 22:17:16 2017

#time.ctime()#将时间戳转化为如下形式Tue Nov 28 22:17:16 2017

#print(time.strftime("%Y-%m-%d %X", time.localtime()))#把一个代表时间的元组或者structur_time转化成固定的时间
#2017-11-28 22:27:07

#time.strptime('2017-11-28 22:27:07','%Y-%m-%d %X')#把一个格式时间转化为structure_time

#把其他格式时间的字符串转化为标准时间字符
# a='2017-11-28 22:27:07'
# timeArray=time.strptime(a,"%Y-%m-%d %H:%M:%S")
# othertime=time.strftime("%Y/%m/%d %H:%M:%S",timeArray)

#通过查看type可以看出标准字符串是时间格式