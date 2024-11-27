'''
fo=open('ex5.txt','w')
import json
po={'name':'kiran','age':23}
jo=json.dumps(po)
print(jo)
fo.write(jo)
'''
'''
fo=open('ex5.txt','w')
import json
po={'name':'kiran','age':23}
print(po)
jo=json.dump(po,fo)
print(jo)
'''
with open('ex5.txt','r') as fo:
    import josn
    jo=fo.read()
    print(jo)
    pd=josn.loads(jo)
    print(pd)
