#动态语言和静态语言最大的不同就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
#type()
#type()函数既可以返回一个对象的类型，又可以创建出新的类型。
def fn(self,name='world'):
    print('Hello,%s' % name)
Hello = type('Hello',(object,),dict(hello=fn))
h = Hello()
h.hello()
print(type(Hello))
print(type(h))
#要创建一个class对象，type()函数一次传入3个参数：
#1.class的名称
#2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法
#3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上
#通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class
#动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂
#除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
#metaclass，直译为元类，简单的解释就是：
#当我们定义了类以后，就可以根据这个类创建出实例，所以先定义类然后创建实例
#但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以先定义metaclass然后创建类。
#连接起来就是：先定义metaclass,就可以创建类，最后创建实例
#所以metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)
class MyList(list,metaclass=ListMetaclass):
    pass
#当我们传入关键字参数metaclass时，魔术生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义
#__new__()方法接收到的参数依次是：
#1.当前准备创建的类的对象
#2.类的名字
#3.类继承的父类集合
#4.类的方法集合
L = MyList()
L.add(1)
print(L)
#ORM Object Relational Mapping 对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样写代码更简单，不用直接操作SQL语句
class Field(object):
    def __init__(self,name,column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__,self.name)
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')
class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)
class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
             raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self,key,value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self,k,None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__,','.join(fields),','.join(params))
        print('SQL:%s' % sql)
        print('ARGS:%s' % str(args))
class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
u = User(id=12345,name='Michanel',email='test@orm.org',password='my-pwd')
u.save()
