'''
IO=iter('hello')
print(next(IO))
print('kirankumat')
print(next(IO))
print(next(IO))
print(next(IO))
print(next(IO))
print(next(IO))
'''
'''
class CIOP:
    def __init__(self,LL,UL,UP=1):
        self.LL=LL
        self.UL=UL
        self.UP=1
    def __iter__(self):
        self.i=self.LL
        return self
    def __next__(self):
        if self.i<self.UL:
            res=self.i
            self.i=self.i+self.UP
            return res
        else:
            raise StopIteration
S=CIOP(1,10)
for i in S:
    print(i)
'''
'''
class CIOP:
    def __init__(self,LL,UL,UP=1):
        self.LL=LL
        self.UL=UL
        self.UP=1
    def __iter__(self):
        self.i=self.LL
        return self
    def __next__(self):
        if self.i<self.UL:
            res=self.i**3
            self.i=self.i+self.UP
            return res
        else:
            raise StopIteration
S=CIOP(1,5)
for i in S:
   print(i)
'''
class CIOP:
    def __init__(self,fv,sv,n):
        self.fv=fv
        self.sv=sv
        self.n=n
    def __iter__(self):
        self.LL=1
        return self
    def __next__(self):
        if self.LL<self.n:
            self.LL=self.LL+1
            res=self.fv
            self.fv=self.sv
            self.sv=res+self.fv
            return res
        else:
            raise StopIteration
K=CIOP(2,3,10)
for i in K:
    print(i)
        
