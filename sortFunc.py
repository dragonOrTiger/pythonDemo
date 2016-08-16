#Python内置的sorted()函数就可以对list进行排序，
print(sorted([36,5,-12,9,-21]))
#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
print(sorted([36,5,-12,9,-21],key=abs))
#默认情况下，对字符串排序，是按照ASCII的大小比较的
print(sorted(["bob","about","Zoo","Credit"]))
#忽略大小写来对字符串排序
print(sorted(["bob","about","Zoo","Credit"],key=str.lower))
#反向排序，不必改动key函数，可以传入第三个参数reverse=true
print(sorted(["bob","about","Zoo","Credit"],key=str.lower,reverse=True))
#我们用一组tuple表示学生名字和成绩，请用sorted()对上述列表分别按名字排序
L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def by_name(stu):
    return stu[0].lower()
L2 = sorted(L,key=by_name)
print(L2)
def by_score(stu):
    return stu[1]
L3 = sorted(L,key=by_score)
print(L3)
