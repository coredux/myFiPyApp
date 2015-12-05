__author__ = 'sr'

class MyDecor( object ):
    def __init__(self , *args , **kw ):
        pass

    def __call__( self , func ):
        def wrapper( *args , **kw ):
            print("Call %s() " % func.__name__ )
            callRet = func( *args , **kw )
            print("Called")
            return callRet
        return wrapper

def callLog( callFunc ):
    def wrapper( *args , **kw ):
        print("Call %s() " % callFunc.__name__ )
        callRet = callFunc( *args , **kw )
        print("Called")
        return callRet
    return wrapper


# 装饰器，把printHello作为参数传进callLog
# 在调用printHello时，实际上是
# printHello = callLog( printHello )
# printHello()

#@callLog # printHello = callLog( printHello )
@MyDecor()
def printHello():
    print("Hello world")

@callLog
def getHelloStr():
    return "Hello world"


if __name__ == "__main__":
    printHello()


