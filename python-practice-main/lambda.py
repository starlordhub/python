'''
def add(n):
    return n+10
print(list(map(add,[22,55,20])))
'''
'''
print(list(map(lambda n:n+10,[44,58,29])))
'''
'''
def iseven(n):
    if n%2==0:
        return True
    else:
        return False
print(list(filter(iseven,[22,55,77,99,44])))
'''
'''
print(list(filter(lambda n:n%2==0,[22,33,55,77,44])))
'''
'''
from functools import reduce
L=[22,33,55,33,66,]
print(reduce(lambda a,b:a if a<b else b,L))
'''
from functools import reduce
L=[22,33,55,66]
print(reduce(lambda a,b:a+b,L))
