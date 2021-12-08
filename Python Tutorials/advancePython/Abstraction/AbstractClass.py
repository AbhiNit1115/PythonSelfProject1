from abc import ABC, abstractmethod


class TV(ABC):  # Abstract class
    @abstractmethod  # decorator for abstract method
    def display(self):  # Not defining the abstract method
        pass

    def smart(self):  # Another method in abstract class which is defined- i.e. concrete method
        print("All TV's are smart")


# We can't create object of Abstract class, hence it becomes the duty of child class to implement the
# method(s) of the parent abstract class.

class Sony(TV):
    def display(self):
        print("Sony has 4k Amoled Display")


class Toshiba(TV):
    def display(self):
        print("Toshiba has 8k Display")


# We are creating object of child classes, we can access the parent abstract class method(S) as well
s = Sony()
s.smart()
s.display()
print()

t = Toshiba()
t.smart()
t.display()
