# create elements and distributes elements of array into buckets
# then sort buckets individually
# finally merge bucket after sorting
# to create bucket use formula: no of buckets = round(sqrt(no. of elements))
clist = [4, 6, 8, 1, 11, 45, 23, 56, 32]  # 9 elements so 3 buckets
# now to know which element wil go to which bucket use formula: cell(value*no. of buckets/ max value)
# so 4 will got to 4 * 3/56 = .2 i.e. first bucket
