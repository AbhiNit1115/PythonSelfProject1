# Accessor Methods:  This method is used to access or read the data of the variables. This method does
# not modifies data in the variable(s) and is also known as "getter method" e.g.
# a standard convention to write getter method is to use "get" (not necessary but standard)
# def get_value(self):
# det get_result(self):
# def get_value(self):

class Mobile:

    def __init__(self):
        self.model = "Nokia 6600"

    def get_model(self):
        return self.model  # via using getter method we are just accessing the data of the variable


company = Mobile()
m = company.get_model()
print(m)


# Mutator Method: This method is used to read or access and modify data of the variables. This method modifies
# the data in the variable and is also known as "setter" method e.g.
# a standard convention to write getter method is to use "set" (not necessary but standard)
# def set_value(self):          class Mobile:                         def set_model(self):
# det set_result(self):             def __init__(self):                      self.model = "iPhone 12"
# def set_value(self):                  self.model = "Nokia 6600


# Setter method without parameter
class Mobile1:

    def __init__(self):
        self.model = "Nokia 6600"  # Instance Variable

    def set_model(self):  # Mutator Method
        self.model = "iPhone 12"  # using setter method we are just modifying the data of the variable


company2 = Mobile1()
# Before setting
print("Before Setting:", company2.model)
# After setting
company2.set_model()
print("After setting:", company2.model)


# Setter method with parameter
class Mobile2:

    def set_model(self, mob):  # Mutator Method
        self.model = mob  # using setter method we are just modifying the data of the variable


company3 = Mobile2()
company3.set_model("Nokia 1100")
print(company3.model)
