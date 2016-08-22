#如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir,cp等命令。
#如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。
import os
#如果是posix,说明系统是Linux、Unix、或Mac OS X,如果是nt,就是Windows系统
print(os.name)
#要获取详细的系统信息，可以调用uname()函数
#注意：uname()函数在Windows上不提供
print(os.uname())
#在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看
print(os.environ)
#要获取某个环境变量的值，可以调用os.environ.get('key'))
print(os.environ.get('PATH'))
print( os.environ.get('x', 'default'))
#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用
print(os.path.abspath('.'))
#把两个路径合成一个时，不要直接拼接字符串，而要通过os.path.join()函数
#这样可以正确处理不同操作系统路径分隔符
#在Linux/Unix/Mac下，os.path.join()返回这样的字符串：part-1/part-2
#在windows下会返回这样的字符串part-1\part-2
os.path.join('/home/syj/gitrepository/pythonDemo','testdir')
os.mkdir('/home/syj/gitrepository/pythonDemo/testdir')
os.rmdir('/home/syj/gitrepository/pythonDemo/testdir')
#同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分是最后级别的目录或文件名
#这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作
print(os.path.split('/home/syj/gitrepository/pythonDemo/IO.py'))
os.rename('test.txt','test.py')
os.remove('test.py')
