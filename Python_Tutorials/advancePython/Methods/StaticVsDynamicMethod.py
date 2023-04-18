# A method is a function in an object's namespace, accessible as an attribute.
# A regular (i.e. instance) method gets the instance (we usually call it self) as the implicit first argument.
# A class method gets the class (we usually call it cls) as the implicit first argument.
# Unlike instance and class method dynamic method gets no implicit first argument (like a regular function).


class Example(object):

    def regular_instance_method(self):
        """A function of an instance has access to every attribute of that
        instance, including its class (and its attributes.)
        Not accepting at least one argument is a TypeError.
        Not understanding the semantics of that argument is a user error.
        """
        return some_function_f(self)

    @classmethod
    def a_class_method(cls):
        """A function of a class has access to every attribute of the class.
        Not accepting at least one argument is a TypeError.
        Not understanding the semantics of that argument is a user error.
        """
        return some_function_g(cls)

    @staticmethod
    def a_static_method():
        """A dynamic method has no information about instances or classes
        unless explicitly given. It just lives in the class (and thus its
        instances') namespace.
        """
        return some_function_h()

# Use dynamic methods when you don't need the class or instance arguments, but the function is related to the
# use of the object, and it is convenient for the function to be in the object's namespace.

# Use class methods when you don't need instance information, but need the class information perhaps for its
# other class or dynamic methods, or perhaps itself as a constructor. (You wouldn't hardcode the class so
# that subclasses could be used here.)
