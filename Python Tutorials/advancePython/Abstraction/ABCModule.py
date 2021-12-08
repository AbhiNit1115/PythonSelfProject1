# Abstract Class: A class derived from ABC class which belongs to abc module is known as abstract class.
# ABC class is known as meta class i.e. a class that defines the behaviour of other class. So we can say that
# Meta class ABC defines that the class which is derived from it becomes an abstract class.
# Abstract class can have abstract method and concrete method.
# Abstract class needs to be extended and its method implemented. We can't create object of an abstract class.


# Abstract Method: An Abstract method is a method whose action is redefined in the child class.
# We can declare a method as abstract by using @abstractmethod decorator
# Abstract method is a method without body.

# Concrete Method: A concrete method is a method whose action is defined in the abstract class itself.
# A concrete method is a method which is defined in the abstract class i.e. method with body.

# Rules: We can't create object of abstract class.
# It is not necessary to declare all abstract method in abstract class
# Abstract class can have abstract and concrete methods.
# If there is any abstract method in class, the class must be abstract.
# The abstract method(s) of an abstract class must be defined in its child class/subclasses.
# If we are inheriting any abstract class that have abstract method, we must provide the implementation
# of the method or make the class abstract.
