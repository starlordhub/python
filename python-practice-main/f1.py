'''
L=[]
for i in range(1,11):
    L.append(i)
print(L)
'''
'''
L=[i for i in range(1,11)]
print(L)
'''
'''
L=[i**2 for i in range(1,11)]
print(L)
'''
'''
L=[22,44,77,20]
d=[i for i in L if i%2==0 and i>30]
print(d)
'''
'''
T=[22,44,77,20]
L=[]
for i in T:
    if i%2==0:
        L.append(1)
    else:
        L.append(0)
print(L)
'''
'''
L=[]
for i in range(1,6):
    for j in range(1,6):
        for k in range(1,6):
            if i=j=k:
                L.append(i,j,k)
print(L)
'''
'''
L[(i,j,k) for i in range(1,6) for i in range(1,6) for k in range(1,6) if i=j=k]
print(L)
'''
s='aBc'
d={s[ip].upper():s[ip].lower()*(ip+1) for ip in range(len(s))}
print(d)

s={'A': 30, 'B': 20, 'C': 10}
enumerate(s)
list(enumerate(s))
print(s)
