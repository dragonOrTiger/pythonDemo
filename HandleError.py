#在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因。在操作系统提供的调用中，返回错误码非常常见。比如打开文件的函数open(),成功时返回文件描述符(就是一个整数)，出错时返回-1
#用错误码来表示是否出错十分不便，因为函数本身应该返回的正常结果和错误码混在一起，造成调用者必须用大量的代码来判断是否出错
def foo():
    r = some_function()
    if r==(-1):
        return (-1)
    return r
def bar():
    r = foo()
    if r ==(-1):
        print('Error')
    else:
        pass
#一旦出错，还要一级一级上报，直到某个函数可以处理该错误(比如，给用户输出一个错误信息)
#所以高级语言通常都是内置了一套try...except...finally...的错误处理机制，Python也不例外
try:
    print('try...')
    r = 10/int('2')
    print('result:',r)
except ValueError as e:
    print('except:',e)
except ZeroDivisionError as e:
    print('except:',e)
else:
    print('no error')
finally:
    print('finally...')
print('END')
#当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕
#此外，如果没有错误发生，可以在except语句块后面加一个else,当没有错误发生时，会自动执行else语句
#Python的错误其实也是class,所有错误类型都继承自Basexception,所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也”一网打尽“
#UnicodeError是ValueError的子类
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:',e)
    finally:
        print('finally...')
main()
#也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了
##################调用堆栈########################

