class Animal(object):
    def run(self):
        print('Animal is running......')
class Dog(Animal):
    def run(self):
        print('Dog is running......')
        def eat(self):
            print('Eating meat......')
class Cat(Animal):
    def run(self):
        print('Cat is running......')
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly......')
dog = Dog()
dog.run()
cat = Cat()
cat.run()
tortoise = Tortoise()
tortoise.run()
print(isinstance(dog,Dog))
print(isinstance(cat,Cat))
print(isinstance(dog,Animal))
print(isinstance(cat,Animal))
print(isinstance(tortoise,Tortoise))
print(isinstance(tortoise,Animal))
def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())
#多态的好处就是，当我们需要传入Dog,Cat,Tortoise,......时，我们只需要接收Animal类型就可以了，因为Dog,Cat，Tortoise......都是Animal类型，然后，按照Animal类型操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思
#对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal,Dog,Cat还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的，这就是著名的”开闭“原则
#对拓展开放：允许新增Animal子类；
#对修改封闭：不需要修改依赖Animal类型的run_twice()等函数
#####################静态语言 vs 动态语言##############################
#对于静态语言来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
#对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
class Timer(object):
    def run(self):
        print('Start......')
run_twice(Timer())
#这就是动态语言的‘鸭子类型’，它并不要求严格的继承体系，一个对象只要”看起来像鸭子，走起路来像鸭子“，那它就可以看做是鸭子。
