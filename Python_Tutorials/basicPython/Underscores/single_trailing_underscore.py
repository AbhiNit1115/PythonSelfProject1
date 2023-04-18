# Sometimes the most fitting name for a variable is already taken by a keyword. Therefore names
# like class or def cannot be used as variable names in Python. In this case you can append a
# single underscore to break the naming conflict:
# e.g.
# def make_object(name, class):
# SyntaxError: "invalid syntax"

def make_object(name, class_):
    pass
