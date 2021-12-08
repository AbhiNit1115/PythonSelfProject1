# In python the interface concept is not explicitly available like other languages.
# In python interface is an abstract class with all abstract methods and no concrete methods at all.

# Rules: All method of interface are abstract and none are concrete.
# We can't create object of interface.
# If a class is implementing interface it has to define all methods of that interface.
# If a class does not implements all method(s) declared in the interface, then the class becomes abstract class

from abc import ABC, abstractmethod


class TV(ABC):  # Interface is same as abstract except all methods are 100% abstract
    @abstractmethod
    def smart(self):
        pass

    @abstractmethod
    def display(self):
        pass


class Sony(TV):  # Child class 1 implementing all the methods of abstract parent class.
    def smart(self):
        print("Sony is a Smart TV.")

    def display(self):
        print("The display is 4k Amoled.")


class Toshiba(TV):  # Child class 2 implementing all the methods of abstract parent class.
    def smart(self):
        print("Toshiba is a Smart TV.")

    def display(self):
        print("The display is 8k.")


s = Sony()  # Object of child class 1
s.smart()
s.display()
print()
t = Toshiba()  # Object of child class 2
t.smart()
t.display()
