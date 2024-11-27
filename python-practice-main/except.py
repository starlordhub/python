'''
print('main star')
L=[11,22,33,55]
try:
    print('try started')
    ip=(int(input('enter index position :')))
    print(L[ip])
    print(a)
    print('try ended')
except IndexError as IE:
    print(IE)
except NameError as NE:
    print(NE)
'''
'''
print('main star')
L=[11,22,33,55]
try:
    print('try started')
    ip=(int(input('enter index position :')))
    print(L[ip])
    print(a)
    print('try ended')
except:
    print('error')
print('main end')
'''
'''
print('main start')
L=[11,22,33,55]
try:
    print('try started')
    ip=(int(input('enter index position :')))
    print(L[ip])
    print(a)
    print('try ended')
except Exception as E:
    print(E)
print('main end')
'''
print('main start')
try:
    print('try started')
    num1=int(input())
    num2=int(input())
    res=num1/num2
    print('try number')
except Exception as E:
    print(E)
else:
    print('inside else block')
    print(res)
finally:
    print('finally is getting ececuted')
print('main end')

