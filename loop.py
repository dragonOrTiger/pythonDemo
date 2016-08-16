names = ["Michanel","Bob","Tracy"]
for name in names:
    print(name)
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)
sum = 0
for x in list(range(1001)):
    sum = sum + x
print(sum)
# 不用list()函数也可以
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
#while循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
