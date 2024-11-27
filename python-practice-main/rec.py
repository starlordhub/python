'''
def sum(num):
    if num==0:
        return 0
    return (num%10)+sum(num//10)
num=1234
print(sum(num))
'''
'''
def fact(val,num):
    if val==num or val==num+1:
        return 1
    return val*fact(val+1,num)
num=2
val=1
print(fact(val,num))
'''
'''
def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
num=5
print(fact(num))
'''

def sum(num,power):
    if num==0:
     return 0 
    return (num%10)**power+sum(num//10,power)
num=157
power=len(str(num))
print('amstrong' if sum(num,power)==num else 'notamstong')

'''
def Even(num):
    if num==45:
        return 0
    if num%2==0:
        print(num)
    Even(num+1)
num=51
Even(num)
'''
'''
def example(n):
    print(n)
    n=n+1
    example(n)
num=1
example(num)
'''
'''
def example(n):
    if n==11:
        return
    print(n)
    example(n+1)
num=1
example(num)
'''
