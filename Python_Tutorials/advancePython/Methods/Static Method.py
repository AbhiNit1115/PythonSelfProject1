# Static methods are used when some processing is related to the class but does not needs the class
# or it's instance(s) to perform any work.
# We use static method when we want to pass some values from outside and perform some action in the method.
# Decorator @staticmethod needs to be written above the static method.
# Syntax: @staticmethod
#         def method_name():
#             method body
# static method without parameter:
class Mobile1:
    fp = "Yes"

    @staticmethod  # Decorator
    def show_model():  # Static method
        # In order to use static method inside write classname.staticmethod name
        print("Fingerprint Available:", Mobile1.fp)


Mobile1.show_model()
print()


# static method with parameter:
class Mobile2:
    fp = "Yes"

    @staticmethod  # Decorator
    def show_model(m, p):  # Static method
        # In order to use static method inside write classname.staticmethod name
        print("Fingerprint Available:", Mobile1.fp)
        model = m
        price = p
        print("Model is:", model)
        print("Price is:", price)


Mobile2.show_model("Nokia 6600", 24000)
