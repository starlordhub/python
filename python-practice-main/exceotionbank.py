'''
def f1():
    print('f1 is started')
    a=10/0
    print('f1 is ended')
def f2():
    print('f2 is started')
    f1()
    print('f2 ia started')
print('main starts')
f2()
print('main end')
'''
'''
def f1():
    print('first line of f1')
    try:
        result=10/0
    except Exception as e:
        print(e)
        print('last line of f1')
def f2():
    print('first line of f2')
    f1()
    print('last line of f2')
    print('main is started')
    f2()
    print('main is ended')
'''
def f1():
    print('f1 is stared')
    a=10/0
    print('f1 is ended')
def f2():
    print('f2 is started')
    f1()
    print('f2 is ended')
print('main start')
try:
    f2()
except Exception as e:
    print(e)
print('main ends')
