def remove_dup(a):
    i = 0
    while i < len(a):
        j = i + 1
        while j < len(a):
            if a[i] == a[j]:
                del a[j]
            else:
                j += 1
        i += 1


s = [1, 2, 2, 3, 4, 4, 5, 2]
remove_dup(s)
print(s)
