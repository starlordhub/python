'''
def fact(num):
    if num==0 or num==0:
        return 1
    return num*fact(num-1)
num=5
print(fact(num))
'''
'''
def sum(num):
    if num==0:
        return 0
    return (num%10)+sum(num//10)
num=1235
print(sum(num))
'''
'''
def mul(num):
    if num==1:
        return 1
    return (num%10)*mul(num//10)
num=1235
print(mul(num))
'''
''''
def fact(val,num):
    if val==num or val==num+1:
        return 1
    return val*fact(val+1,num)
num=2
val=1
print(fact(val,num))
'''
'''
def sum(num,power):
    if num==1:
        return 1
    return (num%10)**power+sum(num//10,power)
num=157
power=len(str(num))
print('its amstorng number' if sum(num,power)==num else 'its not amstorng number')
'''
'''
def sum(num,power):
    if num==1:
        return 1
    return (num%10)**power+sum(num//10,power-1)
num=135
power=len(str(num))
print('its disaram number' if sum(num,power)==num else 'its not disram number')       
'''

def factorial(num):
    if num==1:
        return 1
    return num*factorial(num-1)
def strong(num):
    if num==0:
        return 0
    return factorial(num%10)+strong(num//10)
num=145
print('its strong number'if(strong(num)==num) else 'its not a strong number')

'''
def sqare(num):
    if num==0:
        return 0
    return (num%10)**2+sqare(num//10)
def happy(num):
    if num<10:
        return num==1 or num==7
    return happy(sqare(num))
num=9
'''
print('its happy number' if happy(num) else 'its not happy number')
