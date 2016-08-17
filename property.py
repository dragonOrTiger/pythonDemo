#在绑定属性时，如果我们直接把属性暴露出去，虽然写起来简单，但是没办法检查参数，导致可以把成绩随便改
#这显然不合逻辑，为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value<0 or value>100:
            raise ValueError('score must between 0~100!')
        self._score = value
#现在对任意的Student实例进行操作，就不能随心所欲地设置score了
s = Student()
s.set_score(99)
print(s.get_score())
#但是上面的调用方法又略显复杂，没有直接用属性这么直接简单。
#有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
#Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student1(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer')
        if value<0 or value>100:
            raise ValueError('score must between 0~100')
        self._score = value
s1 = Student1()
s1.score = 99
print(s1.score)
#把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter,负责把一个setter()方法变成属性赋值，于是我们就拥有一个可控的属性操作
#还可定义只读属性，只定义getter方法，不定义setter()方法就是一个只读属性
class Student(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth = value
    @property
    def age(self):
        return 2015-self._birth
#上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来
#########################test########################3
#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,k):
        self._width = k
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,h):
        self._height = h
    @property
    def resolution(self):
        return self._width*self._height
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)

