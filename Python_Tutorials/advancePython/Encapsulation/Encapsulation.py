# Encapsulation in Python describes the concept of bundling data and methods within a single unit.
# So, for example, when you create a class, it means you are implementing encapsulation. A class is an example
# of encapsulation as it binds all the data members (instance variables) and methods into a single unit.
# Also, encapsulation allows us to restrict accessing variables and methods directly and prevent accidental
# data modification by creating private data members and methods within a class.

class Employee:
    def __init__(self, name, project):
        # here name and project are data members
        self.name = name  # --> data member
        self.project = project  # --> data member

    def work(self):  #method
        print("Name is:", self.name, "Project is:", self.project)

# In class we are wrapping data and the methods that work on data within one unit.

# Access Modifiers in Python:
# Encapsulation can be achieved by declaring the data members and methods of a class either as public, private or
# protected. But In Python, we don’t have direct access modifiers like public, private, and protected.
# We can achieve this by using single underscore and double underscores. Access modifiers limit access to the
# variables and methods of a class. Python provides three types of access modifiers private, public,
# and protected.
# Public Member: Accessible anywhere from outside of class.
# Private Member: Accessible within the class
# Protected Member: Accessible within the class and its sub-classes