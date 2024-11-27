'''
s='hello world bye world'
L=[]
word=' '
for ch in s:
    if ch!=' ':
        word=word+ch
    else:
        L.append(word)
        word=' '
L.append(word)
print(L)
'''
'''
s='helloworldbyeworld'
L=[]
word=' '
for ch in s:
    if ch!=' ':
        word=ch+word
    else:
        L.append(word)
        word=' '
L.append(word)
print(L)
'''
'''
s='hello world bye world'
L=[]
word=' '
for ind in range(len(s)-1,-1,-1):
    if s[ind]!=' ':
        word=s[ind]+word
    else:
        L.append(word)
        word=' '
L.append(word)
print(L)
'''

'''
s='hello world bye world'
L=[]
word=' '
for ind in range(len(s)-1,-1,-1):
    if s[ind]!=' ':
        word=word+s[ind]
    else:
        L.append(word)
        word=' '
L.append(word)
print(L)
'''
'''
num=5
spaces=num-1
for val in range(num-1,-1,-1):
    for sp in range(spaces):
        print(' ',end=' ')
    for col in range(num,val,-1):
        print(col,end=' ')
    print()
    spaces-=1
'''
'''
def sum(num,power):
    if num==0:
        return 0
    return (num%10)**power+sum(num//10,power)
num=153
power=len(str(num))
print('Amstrong'if sum(num,power)==num else 'not Amstong number')
'''
'''
def sum(num,power):
    if num==0:
        return 0
    return (num%10)**power+sum(num//10,power-1)
num=135
power=len(str(num))
print('disram'if sum(num,power)==num else 'not disram')
'''
'''
def fact(num):
    if num==1:
        return 1
    return num*fact(num-1)
def strong(num):
    if num==1:
        return 1
    return fact(num%10)+strong(num//10)
num=145
print('strong'if(strong(num)==num) else 'not stong')
'''
def sqare(num):
    if num==0:
        return 0
    return (num%10)**2+sqare(num//10)
def happy(num):
    if num<10:
        return num==1 or num==7
    return happy(sqare(num))
num=13
print('happy'if happy(num) else 'not happy')
    

