'''
with open('pikel.pkl','wb') as f:
     d={'name':'kiran','age':23}
     import pickle
     bo=pickle.dumps(d)
     f.write(bo)
'''
'''
with open('pikel.pkl','wb') as f:
     d={'name':'kiran','age':23}
     import pickle
     bo=pickle.dump(d,f)
'''
with open('pikel.pkl','rb') as f:
     import pickle
     bo=f.read()
     po=pickle.loads(bo)
     print(po)
