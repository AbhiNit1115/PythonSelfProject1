# A hash table is a way of doing key-value lookups. You store the values in an array and then use a hash
# function to find the index of the array cell that corresponds to your key-value pair.

eng_to_esp = {"one": "uno", "two": "dos", "three": "tres"}

# For Key: One, here the hash() will take input as key value which is one and based based on the address of the
# hash function it calculates the index of the element, since the hash function address can be anything so
# based on that the key and it's respective value would be assigned an index the it would move on to next
# key-value pair.