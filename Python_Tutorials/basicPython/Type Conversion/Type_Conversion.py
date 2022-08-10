# Converting one data type into another data type is called as type conversion.

# Implicit Type Conversion: Here python automatically converts one datatype into another. e.g.
a = 5
b = 2
c = a / b
print(type(a))  # This is of integer datatype
print(type(b))  # This is of integer datatype
print(type(c))  # This would be of float datatype
print("______________________________________")
# with implicit type conversion python makes sure that there is no data loss.

# Explicit/Cast Type Conversion: Here user/programmer converts one datatype into another. e.g.
a = 5
b = 2
c = a / b
d = int(c)  # we are explicitly converting the data type of c
print(type(a))  # This is of integer datatype
print(type(b))  # This is of integer datatype
print(d)  # here we are purposefully doing data loss as the result would be integer i.e. 2
print(type(d))  # This would also be of integer datatype as we have changed data type explicitly.
print("__________________________________")

student_class = '10'
student_rollno = 23
clubbed_details = student_rollno + int(student_class)
print(clubbed_details)
print(type(clubbed_details))
