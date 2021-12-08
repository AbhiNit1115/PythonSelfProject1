# Index: An index represents the position number of an array's element e.g.
# stu_rollno = array(i,[101, 102, 103, 104, 105])
# now index always starts from "0", so for above e.g. the following indexing would apply:
# python interpreter allocates 5 blocks of memory and stores these elements.
#    0            1            2            3             4
#   101          102          103          104           105
# stu_roll[0]  stu_roll[1]  stu_roll[0]  stu_roll[3]   stu_roll[4]
# The way to access these arrays is via using stu_roll[index_number]

# Create Array example 1

import array
# there is one more way: from array import *
stu_roll = array.array('i', [101, 102, 103, 104, 105])  # "i" stands for integer
# if we want to use float then use "f"
print(stu_roll[0])
