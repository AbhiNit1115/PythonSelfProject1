# Instance methods are the methods which acts upon the instance variables of the class.
# Instance method needs to know the memory address of the instance which is provided through "self" variable
# by default as first parameter for the instance method.
# "Self" variable has the address of the current object.
# syntax:
# def method_name(self):
# function body

# Instance method without parameter:
class Mobile:
    # constructor
    def __init__(self):
        self.model = "Nokia 6600"  # instance variable

    def show_model(self):  # Instance method
        print("Model Is:", self.model)  # accessing instance variable via instance method


Company = Mobile()  # creating object of class Mobile

# Calling object name without parameter:
# Instance methods are bound to object of a class, so we call instance method with object name:
# Syntax: object_name.method_name()
# Calling Instance method without parameter/argument

Company.show_model()  # here the arguments/parameters are none and the "self" argument is called by default
# hence no need to write self explicitly.


# Instance method with parameter:
class Mobile1:
    # constructor
    def __init__(self):
        self.model = "Nokia 6600"  # instance variable

    def show_model(self, p):  # we are passing one formal argument(p) here
        self.price = p
        print("Model Is:", self.model, "Price is:", self.price)  # accessing the instance variable


# Calling object name with parameter:
# Syntax: object_name.method_name(Actual_argument)

Company_new = Mobile1()
Company_new.show_model(1000)  # we are passing here actual value for the argument "p" for calling
# method with argument
