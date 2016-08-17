#Animal作为超类
#假设我们要实现以下四种动物Dog-狗狗,Bat-蝙蝠,Parrot-鹦鹉,Ostrich-鸵鸟
#如果按照哺乳动物和鸟类归类，我们可以设计出这样的类的层次
#Animal-->Mammal-->Dog
#               -->Bat
#      -->Bird-->Parrot
#             -->Ostrich
#但是如果按照能跑和能飞来归类，我们就应该设计出这样的类的层次
#Animal-->Runnable-->Dog
#                 -->Ostrich
#      -->Flyable-->Parrot
#                -->Bat
#如果要把上面的两种分类都包含进来，我们就得设计更多的层次
#Animal-->Mammal-->MRun-->Dog
#               -->MFly-->Bat
#      -->Bird-->BRun-->Ostrich
#             -->BFly-->Parrot
#如果要再增加宠物类和非宠物类，这么搞下去，类的数量会呈指数增长，很明显这样设计是不行的
#正确的做法是采用多重继承。
class Animal(object):
    pass
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
class RunnableMixIn(Animal):
    def run(self):
        print('Running...')
class FlyableMixIn(Animal):
    def fly(self):
        print('Flying...')
class Dog(Mammal,RunnableMixIn):
    pass
class Bat(Mammal,FlyableMixIn):
    pass
class Parrot(Bird,FlyableMixIn):
    pass
class Ostrich(Bird,RunnableMixIn):
    pass
#在设计类的继承关系时，通常，主线都是单一继承下来的，例如Ostrich继承来自Bird
#但是，如果需要混入额外功能，通过多重继承可以实现，比如，让Ostrich除了继承Bird外，再同时继承Runnable.这种设计通常称之为MixIn.
#为了更好的看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FLyableMixIn.类似地，你还可以定义出肉食动物CarnvorousMixIn和植食动物HerbivoresMixIn,让某个动物同时拥有好几个MixIn
#Python自带的很多库也是用了MixIn.举个例子，Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型有ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来：
