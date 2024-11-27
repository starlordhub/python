'''
with open('kiru.txt','w') as file:
    import json
    po={'name':'ram','age':34,'mobile':(7898,366),'gf':None}
    print(po)
    jo=json.dumps(po)
    print(jo)
    file.write(jo)
'''
with open('kiru.txt','r') as fo:
    import json
    pd=json.load(fo)
    print(pd)

    
