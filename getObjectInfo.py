#当我们拿到一个对象的引用时，如何知道这个对象是什么类型，有哪些方法呢？
###################使用type()#####################
#1.首先我们来判断对象类型，使用type()函数
import sys
print(type(123))
print(type("China"))
print(type(sys))
print(type(abs))
print(type(None))
print(type([1,2,3]))
print(type((1,2,3)))
print(type({"a":1,"b":2,"c":3}))
print(type(set([1,2,3])))
#2.但是type()函数返回的是Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同
print(type(123) == type(456))
print(type(123) == int)
print(type('abc') == type('123'))
print(type('abc') == str)
print(type('abc') == type(123))
#3.判断基本数据类型可以直接写int,str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
import types
def fn():
    pass
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x:x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)
##################使用isinstance()###############################
#1.对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
class Animal(object):
    pass
class Dog(Animal):
    pass
class Husky(Dog):
    pass
a = Animal()
d = Dog()
h = Husky()
print(isinstance(h,Husky))
print(isinstance(h,Dog))
print(isinstance(h,Animal))
print(isinstance(d,Dog))
print(isinstance(d,Animal))
print(isinstance(a,Animal))
#能用type()判断的基本类型也可以用isinstance()判断
print(isinstance('a',str))
print(isinstance(123,int))
print(isinstance(b'a',bytes))
#并且可以判断一个变量是否是某些类型中的一种
print(isinstance([1,2,3],(list,tuple)))
print(isinstance((1,2,3),(list,tuple)))
#####################使用dir()###############################
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，
print(dir("ABC"))
print(len("ABC"))
print("abc".__len__())
#自己写的类，如果也想用len(myobj)的话，就自己写一个__len__()方法
class MyDog(object):
    def __len__(self):
        return 100
mydog = MyDog()
print(len(mydog))
#仅仅把属性和方法列出来是不够的，配合getattr(),setattr(),以及hasattr(),我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x*self.x
obj = MyObject()
print(hasattr(obj,'x'))
print(obj.x)
print(hasattr(obj,'y'))
setattr(obj,'y',19)
print(hasattr(obj,'y'))
print(getattr(obj,'y'))
print(obj.y)
#可以传入一个default参数，如果属性不存在，就返回默认值
print(getattr(obj,'z',404))
print(hasattr(obj,'power'))
print(getattr(obj,'power'))
fn = getattr(obj,'power')
print(fn)
print(fn())
