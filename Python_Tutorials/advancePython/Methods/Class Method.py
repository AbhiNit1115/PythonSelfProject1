# Class methods are the methods which act upon class variable or static variables of the class
# Decorator @classmethod needs to be written above the class method
# By default first parameter of class method is cls which refers to class itself.
# Syntax:- @classmethod --> this is decorator
#          def method_name(cls):
#                   method body

# class method without parameter
class Mobile:
    fp = "Yes"

    @classmethod  # Decorator
    def show_model(cls):  # Class Method
        print("Fingerprint is available:", cls.fp)

    def new_model(self):
        print(f"new model is: {self.fp}")


Mobile.show_model()  # Calling class method
print()


# class method with parameter
class Mobile1:
    fp = "No"

    @classmethod  # Decorator
    def show_model(cls, ram):  # Class Method
        print("Fingerprint is available:", cls.fp)
        print("Ram is:", ram)


Mobile1.show_model("4GB")  # Calling class method
