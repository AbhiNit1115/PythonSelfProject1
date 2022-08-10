# When more than one method with the same name is defined in the same class, it's called method overloading
# Technically in python we can't provide same name to 2 methods so method overloading is not feasible
# But we have one way to achieve it
# In python is a method can perform more than one task it is called method overloading.

class Addition:

    def addition_method(self, b, c, d):
        sum1 = b + c + d
        return sum1


a = Addition()  # creating obj of class Addition
print(a.addition_method(10, 20, 30))  # Calling addition method and passing arguments


# Now the above method is performing addition task but what if we want to pass only 2 values then we will
# give error, but we need to make addition function to perform multiple tasks like addition with 2 numbers
# multiplication etc. so that we can achieve method overloading.

class Calculator:

    def addition_method1(self, b=None, c=None, d=None):

        if b is not None and c is not None and d is not None:
            s = b + c + d
        elif b is not None and c is not None:
            s = b + c
        else:
            print("Please provide 2 numbers for addition")
        return s


c = Calculator()  # creating obj of class Calculator
print(c.addition_method1(10))

