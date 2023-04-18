# In case of selection sort we repeatedly find the minimum element and move it to the sorted part of
# array to make unsorted part sorted. When to use selection sort
# When the array is NOT partially sorted
# When we have memory usage constraints
# When a simple sorting implementation is desired
# When the array to be sorted is relatively small

def selection_sort(custom_list):
    for i in range(len(custom_list)):  # i:0
        min_index = i  # min_index: 0
        for j in range(i + 1, len(custom_list)):  # j: i + 1 means 0 + 1 = 1, j: 1
            if custom_list[min_index] > custom_list[j]:
                #  custom_list[0] i.e. 4(see clist) > custom_list[j] i.e. 6 which is "False"
                # it will iterate until 2 and 3rd index ( 8 and 1 see clist)
                min_index = j
        custom_list[i], custom_list[min_index] = custom_list[min_index], custom_list[i]
    print(custom_list)


clist = [4, 6, 8, 1, 11, 45, 23, 56]
#        0  1  2  3   4   5  6   7
selection_sort(clist)


