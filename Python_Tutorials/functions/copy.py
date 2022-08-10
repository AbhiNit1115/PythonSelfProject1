# The copy() method returns a shallow copy of the list.

my_list = ['cat', 0, 6.7]
# copying a list
new_list = my_list.copy()
print('Copied List:', new_list)  # output: Copied List: ['cat', 0, 6.7]

# If we modify the new_list in the above example, my_list will not be modified.
