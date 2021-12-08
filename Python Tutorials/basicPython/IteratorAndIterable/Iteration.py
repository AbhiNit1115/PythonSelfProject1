list1 = ["Abi", 1.2, "name"]
for i in list1:
    print(i)
# The process of passing from one element to another is called iteration. This for loop will work in the
# same way for the tuples, dictionary, sets, strings.

# In case where we write to program without for loop there are 2 ways: we can use indexing which will work
# for list, tuple, strings but won't work for sets and dictionaries because sets and dictionaries are
# unordered and don't have indexes.

fruits = ['apple', 'orange', 'banana']
i = 0
while i < len(fruits):

    print(fruits[i])
    i = i + 1


# Iterables: for i in list1 --> here the "list1" is called as iterables, everything we can loop over is called
# iterables e.g. list, tuple, sets, dictionaries, sets. Iterables call an inbuilt function iter which will
# give iterators as output.
# Iterables gives iterators to us. Iterator is an object which has only one work to give next element present
# in the iterable e.g. for i in list1, here i is iterable and will give one element everytime the loop is run

