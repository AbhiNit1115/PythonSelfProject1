# os module --This module is used to perform simple operation on directories.
# getcwd() -- This function is used to get the current working directory. syntax os.getcwd()
# chdir() -- this method is used to change current working directory. syntax os.chdir('dirname')
# rename() -- This method is used to change directory name syntax os.rename('oldname', 'newname')
from copy import copy

list_1 = [1, 2, [3, 5], 4]
list_2 = copy(list_1)
list_2[3] = 7
list_2[2].append(6)

print(list_2)
print(list_1)

