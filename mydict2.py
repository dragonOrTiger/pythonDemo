#当我们阅读Python的官方文档，可以看到很多文档都有示例代码。
#这些代码与其他说明可以写在注释中，然后，由一些工具来自动生成文档。既然这些代码本身就可以粘帖出来直接运行，那么可不可以自动执行写在注释中的这些代码呢？
#当我们编写注释时，写上这些示例代码无疑明确告诉函数的调用者该函数的期望输入和输出
#并且Python内置的'文档测试'(doctest)模块可以直接提取注释中的代码并进行测试
#doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。
#只有测试异常的时候，可以用...表示中间一大段烦人的输出
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.
    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1,b=2,c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
   ''' 
    def __init__(self,**kw):
        super(Dict,self).__init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self,key,value):
        self[key] = value
if __name__ == '__main__':
    import doctest
    doctest.testmod()
#还可以通过命令行  python3 -m doctest mydict2.py -v

#doctest非常有用，不但可以用来测试，还可以直接作为示例代码。通过某些文档生成工具，就可以自动把包含doctest的注释提取出来。用户看文档的时候，同时也看到了doctest
