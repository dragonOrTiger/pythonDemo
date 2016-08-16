#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
def now():
    print('2016-08-16')
f = now

f()
#函数对象有一个_name_属性，可以拿到函数的名字
print(now.__name__)
print(f.__name__)
#现在假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为"装饰器"(Decorator)
#本质上，decorator就是一个返回函数的高阶函数
def log1(func):
    def wrapper(*args,**kw):
        print('call %s()' % func.__name__)
        return func(*args,**kw)
    return wrapper
@log1
def now1():
    print('2016-08-16')
now1()
print(now1.__name__)
#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来更复杂。比如自定义log的文本：
def log2(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s()' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
@log2('execute')
def now2():
    print('2016-08-16')
now2()
print(now2.__name__)
#经过decorator装饰之后的函数，它们的__name__已经变成'wrapper'
#因为返回的那个wrapper()函数名字就是wrapper
#所以需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会报错
#不要编写wrapper.__name=func.__name__这样的代码，Python内置的functools.wraps就是干这个事的。
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s()' % func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def func():
    print('16:50:00')
func()
print(func.__name__)
#只需记住在定义wrapper()的前面加上@funtools.wraps(func)即可
