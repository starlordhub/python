def Singletone(arg):
    L=[]
    def inner():
        if not L:
            MCO=arg()
            L.append(MCO)
        return L[0]
    return inner
@Singletone
class Multiplux():
    def __init__(self):
        self.tickets=300
    def booking(self,nt):
        if nt<self.tickets:
            self.tickets=self.tickets-nt
            print('booking is successfull')
            print('remaing tickets',self.tickets)
        else:
            print('tickets are not avalable')
            print('remaing tickets',self.tickets)
shiva=Multiplux()
shiva.booking(200)
print(shiva)
ram=Multiplux()
ram.booking(100)
print(ram)
rams=Multiplux()
rams.booking(100)
print(rams)
