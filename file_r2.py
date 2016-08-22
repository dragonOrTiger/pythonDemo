#但是每次都这样写实在太繁琐，所以Python引入了with语句来自动帮我们调用close()方法
with open('/home/syj/文档/test.txt','r') as f:
    print(f.read())
#这和前面的try...finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
#调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此要根据需要决定怎么调用。
#如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
#for line in f.readlines():
#   print(line.strip())
#像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行
#StringIO就是内存中创建的file-like Object,常用作临时缓冲。
#要读取二进制文件，比如视频，图片等等，用'rb'模式打开文件即可
with open('/home/syj/图片/git-cmd.png','rb') as f:
    print(f.read())
#要读取非UTF-8的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件
with open('/home/syj/文档/测试.txt','r',encoding='gbk') as f:
    print(f.read())
#遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError,因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
# f = open('/Users/michanel/gbk.txt','r',encoding='gbk',errors='ignore')
