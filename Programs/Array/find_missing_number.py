arr = [1, 2, 3, 4, 5, 5, 6, 7, 9, 10]
missing_elements = []
for ele in range(arr[0], arr[-1] + 1):
    if ele not in arr:
        missing_elements.append(ele)
print(missing_elements)


def getMissingNumber(arr):
    # get the array's length
    n = len(arr)

    # actual size is `n+1` since a number is missing from the list
    m = n + 1

    # get a sum of integers between 1 and `n+1`
    total = m * (m + 1) // 2

    # the missing number is the difference between the expected sum and
    # the actual sum of integers in the list
    return total - sum(arr)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 4, 7, 8, 9, 10]

    print('The missing number is', getMissingNumber(arr))
