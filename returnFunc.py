#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
#1.我们来实现可变参数的求和。通常情况下，求和函数是这样定义的
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
print(calc_sum(1,3,5,7,9))
#如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
#可以不返回结果，而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1,3,5,7,9)
print(f)
print(f())
#在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum返回函数sum中，相关参数和变量都保存在返回的函数中，这种成为闭包的程序结构有极大威力
#注意：当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print(1 == f2)
########闭包
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
print(count())
f1,f2,f3 = count()
#上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了
#你可能认为f1(),f2(),f3()结果应该是1,4,9;看看实际结果
print(f1())
print(f2())
print(f3())
#实际结果全部都是9!原因在于返回的函数引用了变量i,但它并非立刻执行。等到三个函数都返回时，它们的引用变量i已经变成了3,因此最终结果为9
#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量
#如果一定要引用循环变量怎么办？方法是在创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count():
    def f(j):
        def g():
            return j*j
        return g
    return map(lambda i:f(i),range(1,4))
#    fs = []
 #   for i in range(1,4):
  #      fs.append(f(i))
   # return fs
print(count())
f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())
