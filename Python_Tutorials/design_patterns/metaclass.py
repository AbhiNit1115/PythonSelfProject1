# Before understanding metaclass, you need to master classes in Python. And Python has a very
# peculiar idea of what classes are, borrowed from the Smalltalk language.
# In most languages, classes are just pieces of code that describe how to produce an object.
# That's kinda true in Python too:

class ObjectCreator(object):
    pass


my_object = ObjectCreator()
print(my_object)
# The output would be <__main__.ObjectCreator object at 0x00000146A4A63FD0>

# But classes are more than that in Python. Classes are objects too.
# Yes, objects.
# As soon as you use the keyword class, Python executes it and creates an object. The instruction creates in
# memory an object with the name ObjectCreator
