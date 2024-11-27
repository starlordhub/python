class ValueError(BaseException):
    def __init__(self,msg):
        self.msg=msg
class Bank:
    def __init__(self,n,a,b,p):
        self.name=n
        self.age=a
        self.balance=b
        self.pin=p
    def withdraw(self):
        try:
            pin=int(input('enter pin :'))
            if pin!=self.pin:
                raise ValueError('incorrect pin :')
            try:
                amount=int(input('enter amount :'))
                if amount>self.balance:
                    raise ValueError('enter valied amount')
                self.balance=self.balance-amount
                print(self.balance)
            except ValueError as E:
                print(E)
        except ValueError as E:
            print(E)
OB=Bank('raju',23,5000,1234)
OB.withdraw()
        
                           
    
