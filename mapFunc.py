##############################################map函数#######################
#map函数接收两个参数，一个是函数，一个是Iterable
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x * x
r = map(f,[1,2,3,4,5,6,7,8,9])
print(r)
print(list(r))
print(list(map(str,[1,2,3,4,5,6,7,8,9])))
#######################################reduce函数############################
#reduce把一个函数作用在一个序列[x1,x2,x3,...]上，这个函数必须接收两个参数
#reduce把结果继续和序列的下一个元素做累积运算
#reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)
from functools import reduce
def fn(x,y):
    return x * 10 + y
r = reduce(fn,[1,3,5,7,9])
print(r)
def str2int(s):
    def fn(x,y):
        return x * 10 + y
    def char2num(s):
        return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[s]
    return reduce(fn,list(map(char2num,s)))
print(str2int("3579"))
##############test 1######################
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def normalize(name):
    return name.capitalize()
L1 = ["adam","LISA","barT"]
L2 = list(map(normalize,L1))
print(L2)
###############test 2####################
#请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(l):
    def ji(x,y):
        return x * y
    return reduce(ji,l)
print(prod([2,4,8]))
############test 3#######################
#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    s = s.split(".")
    frontNum = s[0]
    backNum = s[1]
    backNum = backNum + "0"
    def f1(x,y):
        return x * 10 + y
    def f2(x,y):
        return x/10 + y/10
    def char2Num(s):
        return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[s]
    return reduce(f1,map(char2Num,frontNum))+reduce(f2,map(char2Num,backNum[-1::-1]))
print(str2float("123.456"))
#############################斐波那契数列##########################################
def fib(num):
    n,a,b = 1,0,1
    while n < num:
        yield b
        a,b = b,a+b
        n = n + 1
    return "done"
f = fib(9)
print(fib)
for number in fib(9):
    print(number)
############################杨辉三角形#############################################
def triangles():
    L = [1]
    while(True):
        yield L
        L = [L[x]+L[x+1] for x in range(len(L)-1)]
        L.insert(0,1)
        L.append(1)
    return "done"
n = 0
for t in triangles():
        print(t)
        n = n + 1
        if n == 10:
            break
#######################汉诺塔##############################
def moven(n,a,b,c):
        if n == 1:
            print("move",a,"-->",c)
            return  
        moven(n-1,a,c,b)
        print("move",a,"-->",c)
        moven(n-1,b,a,c)
moven(3,"A","B","C")
