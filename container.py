s = set([1,2,3])
print(s)
s.add(4)
s.add(4)
print(s)
s.remove(2)
print(s)
a = ["c","b","a"]
a.sort();
print(a)
a = "abc"
b = a.replace("a","A")
print(a)
print(b)
c = (1,2,3)
d = (1,[2,3])
a = set([1,2,c])
print(a)
#set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象#是否相等，也就无法保证set内部“不会有重复元素”。
#a = set([1,2,d])
#print(a)
