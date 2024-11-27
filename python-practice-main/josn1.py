






with open('jsondata.txt','r') as fo:
    import json
    jd=fo.read()
    print(jd)
    pd=json.loads(jd)
    print(pd)
    
    

