    # slicing with +ve index [start:stop:stepsize], +ve index move from left to right, so if we give step
# size of 1, then it will move one step size for the given start and stop value from left to right

a = [1, 2, 3, 4, 5, 6]
b = a[0:4:1]  # here index will start from 0 will stop at n-1 i.e. 4-1 =3 and iterate 1 step everytime
# from left to right hence the output would be [1, 2, 3, 4]
print(b)
# Again for +ve index if we give step size as 2 then it will jump two indexes everytime.
c = a[0:5:2]  # here index will start from 0 will stop at n-1 i.e. 5-1 =4 and iterate 2 step everytime
# hence the output would be [1, 3, 5]
print(c)

# Slicing using -ve index consider 2 things:
# 1.) Step size should be -ve
# 2.) Start index should always be greater tha the stop index.

# slicing with -ve index [start:stop:stepsize], -ve index move from right to left, so if we give step size
# of -1, then it will move one step size for the given start and stop value from right to left.
x = [1, 2, 3, 4, 5, 6, 7]
y = x[4:0:-1]  # here index will start from 4th index and iterate -1 step everytime from right to left
# and would stop at the 1st index hence the output would be [5, 4, 3, 2]
print(y)

my_string = "Learning Champion"
# _______________________________________________________
# -16|-15|-14|-13|-12|-11|-10|-9|-8|-7|-6|-5|-4|-3|-2|-1|
#  L |e  |a  |r  |n  |i  |n  |g |C |h | a| m| p| i| o| n|
#  0 |1  |2  |3  |4  |5  |6  |7 |8 |9 |10|11|12|13|14|15|
# ______________________________________________________|
slice1 = my_string[-1:-5:-1]
print(slice1)
# here the string would start from -1 index(n in our case) and would end at -5 index(m in this case) and the
# step would go from right to left with size of -1, output: n o i p

# Scenario 1: No step size while using -ve index
slice2 = my_string[-1:-5]  # here as we haven't given anything python will take this as one
print(slice2)  # the output of this program would be '' as -ve index move from R to L and here we have given
# a positive step size which is contradictory so the start index is now less than stop index which is incorrect.

# Scenario 2: String slicing using a combination of +ve and -ve index
slice3 = my_string[-1:13:-1]
print(slice3)  # this will return noi as the result and not an error even if it violates the second rule here
# that start index (-1) should always be greater tha the stop index(13). Why?? this is because each element
# is represented by a negative as well as positive index. So if step size is -1 even if start index is less
# then  the stop index it would work.

# Scenario3: Slicing using +ve index and -ve step size
slice4 = my_string[7:0:-1]
print(slice4)
# here the output would start from the 7th index till the 0th index but will not include the element at the
# 0th index, hence we can also slice from right to left using step size of -1

# Scenario4: Reverse a string
slice5 = my_string[::-1]
print(slice5)
# as we didn't mentioned ths starting index python would assume this as -1 based on
# the step size that we've given. Also we didn't mentioned the stop so python would assume the first index
# of the string as stop index if step size is -1
