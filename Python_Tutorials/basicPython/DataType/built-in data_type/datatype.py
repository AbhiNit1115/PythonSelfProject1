# Data type represents the type of data that is stored into a variable or memory.
# Python provides 2 types of data types:

# 1.) Built-In Datatype: These data types are provided by Python Language. e.g.
# None Type: It represents an object that doesn't contains any value.
# Numeric Type: It represents an object that contains numeric value e.g. int, float, complex.
# Sequences: Following are the sequence type: String, List, Tuple, Range
# Sets: A set is an unordered collection of elements much like set in maths. The order of the elements is not
# maintained in the sets. It means the elements may not appear in the same order as they are entered into the set.
# A set does not accept duplicate elements. Sets are represented using curly braces {}
# Mapping Type/ Dictionary: A map represents a group of elements in the form of key value pairs

# 2.) User Defined DataType:
# Array
# Class
# Module

mylist1 = [x*x for x in range(3)]
mylist2 = (x*x for x in range(3))
mylist3 = {x: x+x for x in range(1, 3)}
print(mylist1)
print(mylist2)
print(mylist3)
