# Problem Statement: S1 and S2 are given strings
# find the length of the longest subsequence which is common to both strings
# subsequence: a sequence that can be driven from another sequence by deleting some elements w/o changing
# the order of them. e.g. str1 = ABCDE, the subsequence of 3 letters
# ACE, ADE, ACB
# Subsequence of 4 letters: ABCE, ABDE

def find_longest_subsequence(s1, s2, index1, index2):
    # base cond: when we reach the end of any of the str we need to return 0
    if index1 == len(s1) or index2 == len(s2):
        return 0
    # Option1: the char are matching--> will continue to next char by adding 1 to our result
    if s1[index1] == s2[index2]:
        return 1 + find_longest_subsequence(s1, s2, index1 + 1, index2 + 1)
        # index1 + 1 and index 2+1 denotes we continue to next char
    else:  # will write the 2 other options in which char are not matching
        option_1 = find_longest_subsequence(s1, s2, index1+1, index2)
        option_2 = find_longest_subsequence(s1, s2, index1, index2 + 1)
        return max(option_1, option_2)


print(find_longest_subsequence("aroroa", "arora", 0, 0))
