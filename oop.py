#面向对象编程--Object Oriented Programming,简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
#面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。
#而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递
#假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示
std1 = {'name':'Michanel','score':98}
std2 = {'name':'Bob','score':81}
def print_score(std):
    print('%s:%s' % (std['name'],std['score']))
print_score(std1)
print_score(std2)
#如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象，这个对象拥有name和score这两个属性。
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:%s' % (self.name,self.score))
#在Python中定义类是通过class关键字，calss后面紧接着是类名(类名通常是大写开头的单词)，紧接着是(object),表示该类是从哪个类继承下来的。通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
#定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的
#由于类可以起到模板作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name和score等属性绑上去。如果不绑定会报错
#注意到：__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self,因为self就指向创建的实例本身。
#有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不用传，Python解释器自己会把实例变量传进去
#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没什么区别，所以，你仍然可以用默认参数，可变参数，关键字参数和命名关键字参数
#封装的好处：1.可以给类增加新的方法。
#和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
bart = Student('Bart Simpson',59)
print(bart)
lisa = Student('Lisa Simpson',87)
bart.print_score()
lisa.print_score()
#在Class内部,可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
#但是，从前面的Student类的定义来看，外部代码还是可以自由修改一个实例的name,score属性的
bart.score = 95
bart.print_score()
#如果让内部属性不被外部访问，可以把属性的名称前加两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量(private),只有内部可以访问
class Student_new(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s:%s' %(self.__name,self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        self.__score = score
bart = Student_new("Jack",89)
#改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.name和实例变量.score了
#但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法
#如果又要允许外部代码修改score怎么办？可以再给Student类增加set_score方法
#你也许会问，原先那种直接通过bart.score = 59也可以修改啊，为什么要定义个方法大费周折？因为在方法中，可以对参数做检查，避免传入无效的参数
#需要注意：在Python中，变量名类似__xx__，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__,__score__这样的变量名
#有些时候，你会看到以一个下划线开头的实例变量名，比如_name,这样的实例变量外部是可以访问的，但是，按照约定成俗的规定，当你看到这样的变量时，意思就是，”虽然我可以被访问，但是，请把我视为似有变量，不要随意访问“
#双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
#不能直接访问__name是因为Python解释器对外把__name变量改成了_Student_new__name,所以，仍然可以通过_Student_new__name来访问__name变量
#总得来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。
#注意一下下面这种错误写法：
print(bart.get_name())
bart.__name = 'New Name'
print(bart.get_name())
#表面上看，外部代码”成功“设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成_Student_new__name,而外部代码给bart新增了一个__name变量
