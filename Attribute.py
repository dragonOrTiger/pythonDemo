#由于Python是动态语言，根据类创建的实例可以任意绑定属性
#1.给实例绑定属性的方法是通过实例变量，或通过self变量
class Student(object):
    def __init__(self,name):
        self.name = name
s = Student('Bob')
s.score = 90
#2.但是如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有
class Student_new(object):
    name = 'Student_new'
#当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到
s_new = Student_new()
print(s_new.name)#实例并没有name属性，所以会继续查找class的name属性
print(Student_new.name)
s_new.name = 'Michanel'#给实例绑定name属性
print(s_new.name)#由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student_new.name)
del s_new.name#删除实例的name属性
print(s_new.name)#由于实例的name属性没有找到，类的name属性就显示出来了
