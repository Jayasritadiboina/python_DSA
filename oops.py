
from abc import abstractmethod


class A:
    def __init__(self, name, age, gender):  #constructor
        self.__name = name                  #private variable CAN BE ACCESSED  INSIDE OF SAME CLASS WHICH DEFINES WITH __
        self.age = age                      #PROTECTED VARIABLE CAN BE ACCESSED INSIDE OF SAME CLASS AND OUTSIDE OF CLASS WHICH DEFINES WITH _
        self.gender = gender                #PUBLIC VARIABLE CAN BE ACCESSED INSIDE OF SAME CLASS AND OUTSIDE OF ALL CLASSES WHICH DEFINES WITH NO PREFIX
a1=A("jayasri",20,"female")
a2=A("sriram",21,"male")
def display(self):
    print(self.__name)
    print(self._age)
    print(self.gender)
def setAge(self):
    self.age=age
def getAge(self):
    return self.age
a1=A("jayasri",20,"female")
print(a1.display())
a1=setAge(25)
print(a1.getAge())
a2=A("sriram",21,"male")
print(a2.display())
a2=setAge(26)
print(a2.getAge())

#using abstract methods
class BankAccount(ABC):
    def __init__(self,  balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance -= amount
    def get_balance(self):
        return self.__balance
    @abstractmethod
    def interestcalc(self):
        pass
class SavingsAccount(BankAccount):
    def interestrate(self):
        return (0.05)
    
#inheritance
class Animal:
    print("animal sound")
class Dog(Animal):
    def sound(self):
        print("woof")
class Cat(Animal):
    def sound(self):
        print("meow")
    
#polymorphism