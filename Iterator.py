from collections import Iterable
isinstance('Python',Iterable)  #判断实例是否是这个类或者object是变量  #判断是否可以迭代
#迭代器：一定是可迭代对象，拥有next（）方法

from collections import Iterator
a=[11,22,33]
a=iter(a)   #使用iter方法将list转为了一个迭代器
type(a)     #此时a为一个迭代器，可以用next（a）对a循环

# -*-coding:utf-8 -*-
def Fib():
    a,b=0,1
    print("开始")
    for i in range(2):
        print('运行至'+str(i+1)+'次')
        yield b
        print("结束")

#用for循环调用生成器
a=Fib()
for item in a:
    print(item)
#与next等价
# a=Fib()
# a.__next__()
# a.__next__()
# a.__next__()

#<><><><><><><><><><><><><><>
def func():
    i=0
    while i<5:
        item=yield i
        print(item)
        i+=1
f=func()
f.send('Python')  #send在返回值出传入值
f.send('小明')
