# Class variable also know as Static Variable.
# Class variables are variables whose single copy instance is available to all the instance of class
# i.e. When we create object of class in the HEAP memory only one slot will be given to class variable.
# So, if we modify the copy of class variable in one instance, it'll effect all copies of other instance.

# To access class variable(s) we need class methods with cls as first parameter i.e. cls.variable_name

# TO access class variable outside class use Classname.variable_name

class Mobile:
    fp = "Yes"  # this is Class Variable which is defined at class level

    @classmethod  # Inorder to create class method we need to call class method decorator.
    def is_fp(cls):  # Create class method in order to access class variable.
        print(cls.fp)  # We are accessing class variable inside class method.


# To call the class variable outside the class then:
Mobile.fp  # use the class name then dot the variable name
print(Mobile.fp)
Mobile.fp = "No"  # if we want we can change the class variable value as well outside the class.
print(Mobile.fp)


# Another example of class variable

class Mobile2:
    fp = "Yes"  # Class Variable

    def __init__(self):  # Constructor
        self.model = "Nokia 6600"  # Instance Variable

    def show_model(self):  # Instance method to access instance variable
        print("the model is:", self.model)

    @classmethod
    def is_fp(cls):  # class method to access class variable
        print("Is Fingerprint Feature available:", cls.fp)  # accessing class variable
        cls.fp = "No"  # we can even change the class variable value inside class method as well


Company = Mobile2()  # creating object of class Mobile2
Company.show_model()  # Accessing the instance method
Mobile2.is_fp()  # accessing the class method using class name(not object name)
