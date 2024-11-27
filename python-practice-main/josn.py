'''
with open('jsondata.txt','w') as file:
    import json
    po={'name':'kiran','age':23,'mobile':(987,456),'male':True,'female':False,'gf':None}
    print(po)
    jo=json.dumps(po)
    print(jo)
    file.write(jo)
'''
with open('jsondata.txt','r') as fo:
    import json
    
    jd=fo.read()
    print(jd)
    pd=json.load(jd)
    print(pd)
    
    

