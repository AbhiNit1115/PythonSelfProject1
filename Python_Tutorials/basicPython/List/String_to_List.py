a = "abhishek"
b = list(a)
print(b)

c = "abhishek-abhishek-abhishek"
delimiter = '-'
d = c.split(delimiter)
e = list(d)
print(e)

# Implement the method int[] mergeArrays(int[] arr1, int[] arr2) that takes two chronologically sorted
# arrays and returns a new sorted array including all elements from the input arrays.
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
arr3 = []
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] > arr2[j]:
            arr3.append(arr1[i])
print(arr3)

arr41 = [1, 3, 5, 7]
list12 = []
list12['items']

