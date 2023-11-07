def method1(x,y):
    x,y=y,x
    print(x,y)

def method2(x,y):
    x=x+y
    y=x-y
    x=x-y
    print(x,y)

def method3(x,y):
    x=x^y #using XOR
    y=x^y
    x=x^y
    print(x,y)

x,y= map(int,input().split())
method3(x,y)