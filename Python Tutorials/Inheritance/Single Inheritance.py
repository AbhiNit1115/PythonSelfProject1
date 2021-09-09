# If a class is derived from one base class(parent class), it is called single inheritance
# Syntax: class Parentclassname(object):
#              members of parent class
#         class Childclassname(Parentclassname):
#              members of child class

class Appliances:
    appliances = "electric"

    def mixer(self):
        print("This belongs to Parent class and mixer is:", self.appliances)

    @classmethod  # class method is inheritable
    def juicer(cls):
        print("Class Method belonging to Parent class and juicer is:", cls.appliances)

    @staticmethod  # static method is inheritable
    def grinding_stone():
        print("Static Method belonging to Parent class")


class Pluggable(Appliances):

    def is_pluggable(self):
        print("This belongs to child class")


childclass = Pluggable()
childclass.mixer()
childclass.juicer()
childclass.grinding_stone()
childclass.is_pluggable()
