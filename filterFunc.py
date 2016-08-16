#Python内建的filter()函数用于过滤序列
#和map类似，filter也接收一个函数和一个序列。
#和map不同的是，filter把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
#1.在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd,[1,2,4,5,6,9,10,15])))
#2.把一个序列的空字符串删掉，
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,["A","","B",None,"C"," "])))
#Python把0,空字符串，None看成False,其他数值和非空字符串都看成是True
#在计算a and b时，如果a是False,则根据与运算法则，整个结果必定为False,返回a;如果a是True,则整个计算结果必定取决于b,因此返回b
#在计算a or b时，如果a是True，则根据或运算法则，整个计算记过必定为True，因此返回a;如果a是False，则整个计算结果必定取决于b,因此返回b
#3.用filter求素数：计算素数的一个方法是埃氏筛法
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x : x%n > 0 
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
#回数是指从左到右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数
def is_palindrome(num):
    return str(num) == str(num)[::-1]
output = filter(is_palindrome,range(1,1000))
print(list(output))
