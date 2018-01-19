from collections import Iterable
isinstance('Python',Iterable)  #判断实例是否是这个类或者object是变量  #判断是否可以迭代
#迭代器：一定是可迭代对象，拥有next（）方法

from collections import Iterator
a=[11,22,33]
a=iter(a)   #使用iter方法将list转为了一个迭代器
type(a)     #此时a为一个迭代器，可以用next（a）对a循环


