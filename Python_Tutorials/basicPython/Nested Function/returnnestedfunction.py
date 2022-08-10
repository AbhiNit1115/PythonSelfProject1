def display():
    def show():
        return "Show Function: "

    result = show() + "Display Function"
    return result


a = display()
print(a)
print()

# Execution Process: First we are calling the display function then control will go to line number 1
# next from line number 2 to 3 won't be executed as the show function is still not called, next control
# will got to line 5 and then it will execute and then finally control will go to line 5 and then the logic
# inside show function is called.
