#复制文件的函数居然在os模块中不存在！
#原因是复制文件并非有操作系统提供的系统调用。
#理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码
#幸运的是shutil模块提供了copyfile()函数，你还可以在shutil模块中找到很多实用函数，他们可以看作是os模块的补充
import os
print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

