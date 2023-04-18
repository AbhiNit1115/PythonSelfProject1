# Problem statement: S1 and S2 are 2 given string
# Convert S2 to S1 using delete, insert or replace operations.
# Find the min count of edit operations e.g.
S1 = "Catch"
S2 = "Carch"
# Explanation: replace r with t
# No of operations: 1

S3 = "Tbres"
S4 = "Tbres"


# Explanation: Insert 'a' to 2nd position, replace 'r' with 'l' and delete 's'
# No of operations: 3

def find_min_operation(s1, s2, index1, index2):
    # here index 1 and 2 are indexes of 1st and 2nd string.
    # We are checking if the first index = len of first string
    if index1 == len(s1):  # means we have reached the end of s1
        return len(s2) - index2  # we need to delete the rest char from s2
    # now next base cond. if we have reached the end of s2 the rest char from s1 need to be added to s2
    if index2 == len(s2):
        return len(s1) - index1  # we need to add char from s1 to s2
    # now next base cond. if char are matching from both strings the continue to next char of both strings
    if s1[index1] == s2[index2]:
        return find_min_operation(s1, s2, index1 + 1, index2 + 1)
    else:  # in else cond as well we need to divide this prob into 3 sub prob and find min operation from this
        delete_op = 1 + find_min_operation(s1, s2, index1, index2 + 1)
        # here 1+ denotes the no. of operations so only delete then 1, d+insert =2, d+i+replace = 3
        insert_op = 1 + find_min_operation(s1, s2, index1 + 1, index2)
        replace_op = 1 + find_min_operation(s1, s2, index1 + 1, index2 + 1)
        return min(delete_op, insert_op, replace_op)


print(find_min_operation("table", "tbres", 0, 0))
