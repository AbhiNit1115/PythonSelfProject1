# Object: Object is a class type variable or class instance. In order to use a class we should create
# an object of the class.
a = 10
print(type(a))  # here a is a variable whose type(datatype) is of integer


# Similarly object is a variable of "class" type.


class A:

    def test_class(self):
        print("class example")


obj = A()  # here obj would be called a variable whose type is class.
print(type(obj))

# Object/Instance creation represents allocating memory necessary to store the actual data of the variables.
# Each type we create an object of the class a copy of each variable(s) that is defined in the class is created.
# In other words we can say that each object of a class has its own copy of data members defined in the class.
