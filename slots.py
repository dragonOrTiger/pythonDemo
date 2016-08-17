#正常情况下，当我们定义了一个class,创建了一个class的实例后，我们可以给该实例绑定任何属性和方法
class Student(object):
    pass
s = Student()
s.name = 'Michanel'
print(s.name)
#还可以给实例绑定一个方法：
def set_age(self,age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)
#但是，给一个实例绑定的方法，对另一个实例是不起作用的
#为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self,score):
    self.score = score
Student.set_score = set_score
#给class绑定方法后，所有实例均可调用
s1 = Student()
s1.set_score(100)
s2 = Student()
s2.set_score(99)
print(s1.score,s2.score)
#但是我们想要限制实例的属性怎么办？比如只允许Student实例添加name和age属性
#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class StudentNew(object):
    __slots__ = ('name','age')
sn = StudentNew()
sn.name = 'Bob'
sn.age = 25
print(sn.name,sn.age)
#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudentNew(StudentNew):
    pass
g = GraduateStudentNew()
g.name = 'jack'
g.age = 26
g.score = 89
print(g.name,g.age,g.score)
