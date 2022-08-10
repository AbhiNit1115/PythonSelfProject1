def display():
    def show():
        print("This is inner show function")
    print("This is outer display function")
    show()

a = display()
print(a)
print()


# Execution Process: First we are calling the display function then control will go to line number 1
# next from line number 2 to 3 won't be executed as the show function is still not called, next control
# will got to line 4 and then it will execute and then finally control will go to line 5 and then the logic
# inside show function is called.



def display1():
    def show1():
        print("This is inner show function")
    show1()
    print("This is outer display function")


a1 = display1()
print(a1)

# Execution Process: First we are calling the display function then control will go to line number 19
# next from line number 20 to 21 won't be executed. Now in line 22 the show function is getting called
# so the inner function will execute then finally control will go to line 23 and then the logic
# inside outer function i.e. display  is called.
