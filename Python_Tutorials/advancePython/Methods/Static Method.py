# Static methods are used when some processing is related to the class but does not needs the class
# or it's instance(s) to perform any work.
# We use dynamic method when we want to pass some values from outside and perform some action in the method.
# Decorator @staticmethod needs to be written above the dynamic method.
# Syntax: @staticmethod
#         def method_name():
#             method body
# dynamic method without parameter:
class Mobile1:
    fp = "Yes"

    @staticmethod  # Decorator
    def show_model():  # Static method
        # In order to use dynamic method inside write classname.staticmethod name
        print("Fingerprint Available:", Mobile1.fp)


Mobile1.show_model()
print()


# dynamic method with parameter:
class Mobile2:
    fp = "Yes"

    @staticmethod  # Decorator
    def show_model(m, p):  # Static method
        # In order to use dynamic method inside write classname.staticmethod name
        print("Fingerprint Available:", Mobile1.fp)
        model = m
        price = p
        print("Model is:", model)
        print("Price is:", price)


Mobile2.show_model("Nokia 6600", 24000)


# ______________________________________________________________________________ #

class calculator:

    def __init__(self, version: int):
        self.version = version

    def description(self):
        print(f'the version of the calculator is {self.version}')

    # now here you can see that python gives a suggestion that may be static method i.e. this method is
    # static i.e. it can be used anywhere and doesn't relies on the class and if we do a quick fix then
    # python will put this method outside of the class.
    def add_numbers(self, *numbers: float) -> float:
        return sum(numbers)


# ______________________________________________________________________________ #
# now to make user aware that the static method is relevant to the class we just use the decorator
# @staticmethod so that anyone who is looking into this code can understand that this static ,method
# is relevant for this class and they won't create this method outside.

class calculator1:

    def __init__(self, version: int):
        self.version = version

    def description(self):
        print(f'the version of the calculator is {self.version}')

    # now here you can see that python gives a suggestion that may be static method i.e. this method is
    # static i.e. it can be used anywhere and doesn't relies on the class and if we do a quick fix then
    # python will put this method outside of the class.
    @staticmethod
    def add_numbers(*numbers: float) -> float:
        return sum(numbers)
