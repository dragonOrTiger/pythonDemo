#很多时候，数据读写不一定是文件，也可以在内存中读写。
#StringIO顾名思义就是在内存中读写str
#要把str写入StringIO我们需要先创建一个StringIO，然后，像文件一样写入即可
#getvalue()方法获得写入后的str
from io import StringIO
with StringIO() as f:
    f.write('hello')
    f.write(' ')
    f.write('world!')
    print(f.getvalue())
#要读取StringIO,可以用一个str初始化StringIO，然后，像读文件一样读取
with StringIO('Hello!\nHi!\nGoodbye!') as f:
    while True:
        s = f.readline()
        if s == '':
            break
        print(s.strip())
