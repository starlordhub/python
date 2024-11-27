'''
f=open('kumar.txt','r')
data=f.readline(10)
print(type(data))
print(data)
'''

f=open('kumar.txt','r')
data=f.readlines()
print(data)
print(type(data))
f.seek(10)
print(f.tell())

'''
fo=open('kumar.txt','r')
print(fo.name)
print(fo.mode)
print(fo.close)
print(fo.readable())
print(fo.writable())
'''
'''
with open('kumar.txt','w') as fo:
    fo.write('this data will be save the')
    print(fo.closed)
print(fo.closed)
'''
