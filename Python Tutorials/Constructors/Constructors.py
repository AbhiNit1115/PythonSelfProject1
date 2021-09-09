# A constructor is called as soon as we create any Object of a class i.e.
# A constructor is "Called" automatically.
# Two types of Constructors i.e. with and without parameters

# Example of constructor without parameter
class Mobile:
    def __init__(self):
        self.model = "nokia"

    def show_model(self):
        print("Model:", self.model)


company = Mobile()
company.show_model()
print()


# Example of constructor with parameter
class Phone:
    # constructor
    def __init__(self, m, v=80):
        self.model = m
        self.volume = v

    def show_model(self, p):
        price = p
        print("Model:", self.model, "and Price:", p)
        print("Volume:", self.volume)


# In this step we are creating object of class Mobile and passing argument value for 'm'
# for v there is already one default value if we want we can pass argument value for v or leave it.
Company2 = Phone("Samsung")
# In this step we are passing the argument value for p i.e. price that we have created in the show_model method
Company2.show_model(1000)
