def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    bar('0')
main()
########################错误信息#############################
#Traceback (most recent call last):
#    File "err.py", line 7, in <module>
#        main()
#    File "err.py", line 6, in main
#        bar('0')
#    File "err.py", line 4, in bar
#        return foo(s)*2
#    File "err.py", line 2, in foo
#        return 10/int(s)
#ZeroDivisionError: division by zero
###########################错误信息##################################
#第1行告诉我们这是错误的跟踪信息
#第2~3行：调用main()出错了，在代码文件err.py的第7行代码，但原因在第6行
#第4~5行：调用bar('0')出错了，在代码文件err.py的第6行代码，但原因在第4行
#第6~7行：调用foo(s)*2出错了，在代码文件err.py的第4行代码，但原因在第2行
#第8~9行：调用10/int(s)出错了，在代码文件err.py的第2行代码，这是错误源头
#第10行打印了根本的错误原因
