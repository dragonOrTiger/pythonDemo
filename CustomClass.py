#看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的
#__slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数
#除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类
#1.__str__
class Student(object):
    def __init__(self,name):
        self.name = name
print(Student('Michanel'))
#打印出：<__main__.Student object at 0x7f4dc9236eb8>
#怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了
class Student1(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student object(name:%s)' % self.name
print(Student1('Michanel'))
#但是细心的朋友会发现直接敲变量不用print,打印出来的实例还是不好看
#这是因为直接显示变量调用的不是__str__(),而是__repr__(),两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
#解决办法是在定义一个__repr__.但是通常__str__()和__repr__()代码都是一样的，所以可以直接写__repr__ = __str__
#2.__iter__
#如果一个类想被用于for...in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，知道遇到StopIteration错误时退出循环
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a
for n in Fib():
    print(n)
#Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第五个元素：print(Fib()[5])
#__getitem__
#要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
class Fib1(object):
    def __getitem__(self,n):
        a,b = 1,1
        for x in range(n):
            a,b = b,a+b
        return a
print(Fib1()[0])
print(Fib1()[1])
print(Fib1()[2])
print(Fib1()[3])
print(Fib1()[10])
print(Fib1()[100])
#但是list有个神奇的切片方法，对于Fib却报错。原因是__getitem__()传入的传入的参数可能是一个int，也可能是一个切片对象slice,所以要判断：
class Fib2(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b,a+b
            return L
print(Fib2()[:10])
#但是没有对ste参数做处理
#没有对负数做处理，所以要正确实现一个__getitem__()还是有很多工作要做的。
#此外，如果对象看成dict,__getitem__()的参数也可能是一个可以做key的object,例如str
#与之对应的__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素
#3.正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错
#__getattr__
class Student2(object):
    def __init__(self):
        self.name = 'Michanel'
s2 = Student2()
print(s2.name)
#调用name属性，没问题
#但是调用不存在的score属性，就有问题了
# AttributeError: 'Student2' object has no attribute 'score'''''
#要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。
class Student3(object):
    def __init__(self):
        self.name = 'Michanel'
    def __getattr__(self,attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda:25
        raise AttributeError("'Student3' object has no attribute '%s'" % attr)
#当调用不存在的属性时，，比如score,Python解释器会试图调用__getattr__(self,'score')来尝试获得属性，这样就有机会返回score的值
s3 = Student3()
print(s3.name)
print(s3.score)
print(s3.age())
#注意：只有在没有找到属性的情况下，才调用__getattr__()，已有的属性，比如name,不会在__getattr__中查找
#此外，注意到任意调用如s.abc都会返回None,这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误
class Chain(object):
    def __init__(self,path=''):
        self._path = path
    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path,path))
    def __str__(self):
        return self._path
    __repr__ = __str__
print(Chain().status.user.timeline.list)
#一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
#能不能直接在实例本身上调用呢？
#在Python中，答案是肯定的
#任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
class Student4(object):
    def __init__(self,name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)
s4 = Student4('Michanel')
s4()
#__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为两者之间本来就没啥根本区别
#如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来的，因为类的实例都是运行期创建出来的，这么以来，我们就模糊了对象和函数的界限
#那么如何判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象。比如函数和__call__()的实例
print(callable(Student4('Bob')))
print(callable(max))
print(callable([1,2,3]))
print(callable(None))
print(callable('str'))

