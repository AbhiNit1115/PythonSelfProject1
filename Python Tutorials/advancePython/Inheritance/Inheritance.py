# All classes in python are build from a single super class called "object", so whenever we create
# a class in python, object will become super class for them internally
# we usually create class like this:
# class Mobile:
# but internally its happening like
# class Mobile(object):
# This object we don't need to explicitly specify
# Types of Inheritance : Single, Multi-Level, Multiple, Hierarchical etc.
class Employee:

    def __init__(self, d):
        print('Employee created')
        self.department = d

    def __del__(self):
        print("Destructor called")

    def emp_dept(self):
        print("Employee Department is:", self.department)


def Create_obj():
    print('Making Object...')
    obj = Employee("sales")
    print('function end...')
    obj.emp_dept()
    return obj


print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')
