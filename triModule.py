#在Python中，安装第三方模块，是通过包管理工具pip完成的
#pip            pip3.4
#一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：sudo pip3.4 install Pillow
from PIL import Image
im = Image.open('git-cmd.png')
print(im.format,im.size,im.mode)
im.thumbnail((200,100))
im.save('git_cmd.jpg','JPEG')
###################模块搜索路径###################################
#1.默认情况下，Python解释器会搜索当前目录，所有已安装的内置模块和第三方模块
#搜索路径存放在sys模块的path变量中
import sys
print(sys.path)
#################添加自己的搜索目录有两种方法###################
#1.直接修改sys.path，添加要搜索目录：sys.path.append('path')
#这种方法是在运行时修改，运行结束后失效
#2.第二种方法是设置环境变量PYTHONPATH，该环境变量的内容被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。
# export PYTHONPATH=$PYTHONPATH:/home/lxc/software/program/python
