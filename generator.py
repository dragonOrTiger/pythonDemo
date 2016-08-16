from collections import Iterable
g = (x*x for x in range(10))
print(g)
print(isinstance(g,Iterable))
for n in g:
    print(n)
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n + 1
    return "done"
fib(8)
#把print(b)改为yield b 就成generator了
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n + 1
    return "done"
f = fib(6)
print(f)
for n in f:
    print(n)
def triangles():
    L = [1]
    while True:
        yield L
        L = [L[x]+L[x+1] for x in range(len(L)-1)]
        L.insert(0,1)
        L.append(1)
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

