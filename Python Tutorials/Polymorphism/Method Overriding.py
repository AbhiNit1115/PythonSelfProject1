# If we write method in both class i.e. parent as well as child class then the parent class method object
# is not available to the child class. In this case only child class method object is accessible which
# means child class method is replacing parent class method.

class Mammal:

    def mammal_bmi(self, oxygen, heartbeat):
        bmi = oxygen + heartbeat
        print(bmi)


class Dog(Mammal):

    def mammal_bmi(self, carbon, heartbeat):
        bmi = carbon * heartbeat
        print(bmi)


d = Dog()  # creating object of child class dog
d.mammal_bmi(10, 15)  # here the child class method is called and performing multiplication to get BMI.


# If we write method in both the classes i.e. parent and child then parent class method is not available
# to child class in this case only child class method is accessible.
# super() methods id used to class parent class constructor or method(s) from child class
# syntax: super().methodName()

class Mammal1:

    def mammal_bmi1(self, oxygen, heartbeat):
        bmi = oxygen + heartbeat
        print(bmi)


class Dog1(Mammal1):

    def mammal_bmi1(self, carbon, heartbeat):
        bmi = carbon * heartbeat
        super().mammal_bmi1(10, 15)  # we need to pass the arguments for parent class method along with the
        # super method in the child class method itself.
        print(bmi)


d1 = Dog1()
# here the arguments that we are passing will got to child class method's bmi and the arguments that we
# have passed in the super method mammal_bmi1 will got to parent class method mammal_bmi1
d1.mammal_bmi1(23, 33)
