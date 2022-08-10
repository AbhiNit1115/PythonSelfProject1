# Please read Class Variable before this
# Namespace represents a memory block where names are mapped to objects. It's of 2 types
# Class Namespace: A class maintains it's own namespace aka class namespace. In class namespace names are
# mapped to class variables
# Instance Namespace: EVery instance has it's own namespace aka Instance namespace. In Instance namespace
# names are mapped to instance variables

class Mobile:
    fp = 'Yes'  # This fp variable name is pointing towards the value "Yes" this is what we call namespace
    # i.e. where our class variable is getting mapped with a name

    @classmethod
    def is_fp(cls):
        print("Is finger Print available?", cls.fp)


Company = Mobile()
Brand = Mobile()
Order = Mobile()

print("Class FP:", Mobile.fp)
print("Company FP:", Company.fp)
print("Brand FP:", Brand.fp)
print("Order FP:", Order.fp)

print()
# Now we modify the value inside the class variable using class name
Mobile.fp = "No"
# Now we run the print again then all the objects will have the same updated value of class variable
# Because class variable has only one copy and the same copy is shared with all the instance(s)
print("Class FP:", Mobile.fp)
print("Company FP:", Company.fp)
print("Brand FP:", Brand.fp)
print("Order FP:", Order.fp)

print()
# Now we are going to update the class variable in one object only
Brand.fp = 'Updated value of class variable only for this brand object'
print("Class FP:", Mobile.fp)
print("Company FP:", Company.fp)
print("Brand FP:", Brand.fp)
print("Order FP:", Order.fp)
