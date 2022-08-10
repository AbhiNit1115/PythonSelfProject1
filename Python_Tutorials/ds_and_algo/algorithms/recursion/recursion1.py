# The below mentioned methods would go and get stored in the "Stack Memory" which works on the concept of
# Last In First Out LIFO
class Recursion:

    # Now as soon as the program executes the control would go the the first line of first method which is calling
    # second method so first_method() would go and store in the stack memory
    def first_method(self):
        self.second_method()
        print("I'm first method")

    # Now as soon as the program executes the control would go the the first line of second method which is calling
    # third method so second_method() would go and store in the stack memory just after first method
    def second_method(self):
        self.third_method()
        print("I'm second method")

    # Now as soon as the program executes the control would go the the first line of third method which is calling
    # fourth method so third_method() would go and store in the stack memory after first and second method
    def third_method(self):
        self.fourth_method()
        print("I'm third method")

    # Now the control would come to 4th method and this will execute.
    def fourth_method(self):
        print("I'm fourth method")


# Now as per the Stack Memory Lifo concept the last in method after 4th method was 3rd method then 2nd then 1st
# so the printing order would be
# I'm fourth method
# I'm third method
# I'm second method
# I'm first method
