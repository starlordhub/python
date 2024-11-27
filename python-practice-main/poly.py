'''
class Animal:
    def move1(self):
        print('animal is moving')
class Dog(Animal):
    def move(self):
        print('dog is barking')
obj=Dog()
obj.move()
obj.move1()
'''
'''
class Mod:
    def __init__(self):
        self.var=59
    def method(self):
        print(self.var)
obj=Mod()
print(obj.var)
obj.method()
'''
'''
class Mod:
    def __init__(self):
        self._var=59
    def method(self):
        print(self._var)
obj=Mod()
print(obj._var)
obj.method()
'''
'''
class Mod:
    def __init__(self):
        self.__var=59
    def method(self):
        print(self.__var)
obj=Mod()
obj.method()
print(obj.__var)
'''
class A:
    x=29
    _y=34
    __z=35
@classmethod
def get_pd(cls):
    print(cls.__z)
def .display(self):
    print('its is public class')
def ._show(self):
    print('its is a protect class')
def .__secrd(self):
    print('its is  public class')
print(A.x)
print(A._y)
print(A._A__z)
OA=A()
OA.display()
OA._show()
OA._A__secrd()
