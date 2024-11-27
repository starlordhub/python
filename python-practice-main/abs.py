from abc import ABC,abstractmethod
class Kali(ABC):
    @abstractmethod
    def breakfast(self):
        pass
    @abstractmethod
    def lunch(self):
        pass
    @abstractmethod
    def dinner(self):
        pass
class Ram(Kali):
    def breakfast(self):
        print('edli with sambar')
    def lunch(self):
        print('rice with vada')
    def dinner(self):
        print('chapathi with cury')
obj=Ram()
obj.breakfast()
class Vasu(Kali):
    def breakfast(self):
        print('ponga and vada')
    def lunch(self):
        print('rice with rasam')
    def dinner(self):
        print('dhosa whith ch')
obj1=Vasu()
obj1.breakfast()
