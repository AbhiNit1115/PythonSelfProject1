class Mobile:

    # Instance variable is written inside the class constructor
    def __init__(self):
        # The instance variable name will have "self." and the name of the variable
        self.model = "Micromax"  # This is our "Instance Variable"

    def show_model(self):  # This is our Instance method for accessing instance variable.
        print("The Mobile brand is:", self.model)  # We are accessing Instance Variable inside Instance Method


Company = Mobile()  # created object of class Mobile
# Here we are accessing the instance variable outside class by using object name
print("The Brand Name is:", Company.model)
# We can change the value of instance variable as well by using the object name
Company.model = "Redmi"
print("The Brand Name is:", Company.model)

# Instance variables separate copy is created for every object
# If we modify copy of instance variable in an instance, it will not affect copy of other instance(s)
Company = Mobile()  # we have created three different objects of class Mobile
Product = Mobile()
Order = Mobile()

Company.model = "Samsung"  # we have changed the value of instance variable for Company object
Product.model = "Nokia"  # we have changed the value of instance variable for Product object
Order.model = "Apple"  # we have changed the value of instance variable for Order object

# Now for all the three above objects different memory would be allocated in the HEAP
# And separate copies of instance variables would be created for each object.
print("The Company Name is:", Company.model)
print("The Product is:", Product.model)
print("The Order is for:", Order.model)
