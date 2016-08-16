#可以直接作用于for循环的数据类型有以下几种：
#一类是集合数据类型，如list,tuple,dict,set,str
#一类是generator,包括生成器和带yield的generator function
#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
#可以使用isinstance()判断一个对象是否是Iterable对象。需导入collections的Iterable对象
###########################################################################
#而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，
#知道最后抛出StopIteration错误表示无法继续返回下一个值了
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
#可以使用isinstance()判断一个对象是否是Iterator对象
from collections import Iterator
print(isinstance([x for x in range(10)],Iterator))
print(isinstance((x for x in range(10)),Iterator))
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance("abc",Iterator))
#生成器都是Iterator对象，但list,tuple,str,dict虽然是Itrable,但不是Iterator
#把list,dict,str,等变成Iterator,可以用iter()函数
print(isinstance(iter([]),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter("abc"),Iterator))

