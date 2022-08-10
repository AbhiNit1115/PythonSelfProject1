# Singleton are a design pattern where only one instance may exist at any given time.
# This pattern relies on 2 mechanism of Object Orientation: first is a static/class method that gives access
# to an instance of a class, second is the private access modifier that allows access to a method only from
# inside the class by making the constructor private only the static method inside the class can create an instance.
# Used in case of data configuration like DB connectivity, WebDriver Manager etc.

# Ways to achieve Singleton in Python:
# 1.) Using static method
class DBConnection:
    """This is a class variable and will keep track whether our instance is created or not
        when we say instance = none means that when our program runs the instance is not yet created"""
    __db_instance = None

    @staticmethod
    def get_db_instance():
        if DBConnection.__db_instance is None:  # if the instance inside class DBConnection is none then
            DBConnection()  # we are going to create a Singleton object for DB
        return DBConnection.__db_instance

    def __init__(self):
        if DBConnection.__db_instance is not None:
            try:
                print("the connection is ", DBConnection.__db_instance)
            except BaseException:
                print("Exception")
        else:
            DBConnection.__db_instance = self


db1 = DBConnection.get_db_instance()
print(db1)
db2 = DBConnection.get_db_instance()
print(db2)
print("___________________________________________")


# 2.) Using class method
class WebDriver:
    """This is a class variable and will keep track whether our instance is created or not
        when we say instance = none means that when our program runs the instance is not yet created"""
    __webdriver_instance = None

    # when first time we are going to create WebDriver obj its gonna run this __new__ method then
    def __new__(cls, *args, **kwargs):
        if cls.__webdriver_instance is None:  # it will see that there are no web driver instances
            # then its going to create it
            cls.__webdriver_instance = super(WebDriver, cls).__new__(cls, *args, **kwargs)
        return cls.__webdriver_instance


wd1 = WebDriver()
print(wd1)
wd2 = WebDriver()
print(wd2)
print("___________________________________________")


# 2.) Using a meta class
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    pass


t1 = MyClass
print(t1)
t2 = MyClass
print(t2)

