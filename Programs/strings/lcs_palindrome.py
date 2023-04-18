def lcs_palindrome(str1, start_index, end_index):
    if start_index > end_index:
        return 0
    elif start_index == end_index:
        return 1
    elif str1[start_index] == str1[end_index]:
        return 2 + lcs_palindrome(str1, start_index+1, end_index-1)
    else:
        op1 = lcs_palindrome(str1, start_index, end_index-1)
        op2 = lcs_palindrome(str1, start_index+1, end_index)
        return max(op1, op2)


print(lcs_palindrome("arora", 0, 3))
