#当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便
print(list(map(lambda x : x*x,[1,2,3,4,5,6,7,8,9])))
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
#用匿名函数有个好处：因为函数没有名字，不必担心函数名冲突
#匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f = lambda x : x*x
print(f)
print(f(5))
#同样可以把匿名函数作为返回值返回
def build(x,y):
    return lambda:x*x + y*y
f = build(3,4)
print(f())
