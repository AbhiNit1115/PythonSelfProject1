# The below mentioned methods would go and get stored in the "Stack Memory" which works on the concept of
# Last In First Out LIFO

# Now as soon as the program executes the control would go the the first line of first_method which is calling
# second method so first_method() would go and store in the stack memory
def first_method():
    second_method()
    print("I'm first method")


# Now as soon as the program executes the control would go the the first line of second_method which is calling
# third_method so second_method() would go and store in the stack memory just after first_method
def second_method():
    third_method()
    print("I'm second method")


# Now as soon as the program executes the control would go the the first line of third_method which is calling
# fourth_method so third_method() would go and store in the stack memory after first and second method
def third_method():
    fourth_method()
    print("I'm third method")


# Now the control would come to 4th method and this will execute.
def fourth_method():
    print("I'm fourth method")


# Now as per the Stack Memory Lifo concept the last in method after 4th method was 3rd method then 2nd then 1st
# so the printing order would be
# I'm fourth method
# I'm third method
# I'm second method
# I'm first method

m1 = first_method()


# Now lets use recursion and understand

def recursive_method(n):
    if n < 1:
        print("{} is less than 1".format(n))
    else:
        recursive_method(n - 1)
        print(n)


re = recursive_method(4)

# When this code executes the the control will go check if 4 < 1 the for which the condition is not satisfied so
# recursive method(4) will go and get stored in stack memory first then it will check for 3 < 1 again
# recursive method(3) will go and get stored in stack memory after recursive method(4) then it will check for 2
# recursive method(2) will go and get stored in stack memory after recursive method(3) and (4) then same with 1
# recursive method(1) will go and get stored in stack memory after recursive method(2), (3) and (4).
# Now when it gets 0 then condition gets satisfied now we need to check for exit statement which will execute
# as soon as it finds the satisfied condition. Now as per LIFO the program will go and check which is the last in
# in our case its recursive method(1) after which recursive method(2), recursive method(3) and in the last
# recursive method(4) so as soon as the the method is executed the stack memory becomes free.

# 1.) Stack Memory is used by the system to manage recursive calls.
# 2.) Every time the recursive method calls itself the system stores it in a stack for coming back because there
# are execution statements left after calling itself
