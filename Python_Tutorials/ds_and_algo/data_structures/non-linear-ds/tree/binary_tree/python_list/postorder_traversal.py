class BinaryTree:

    def __init__(self, size):
        self.size = size
        self.custom_list = size * [None]  # based on size param we initialize fixed size custom list
        self.last_used_index = 0  # to skip the 0th index
        self.max_size = size

    def insert_node(self, value):
        if self.last_used_index + 1 == self.max_size:
            return "The Binary Tree is full"
        self.custom_list[self.last_used_index + 1] = value  # insert values to the custom list
        self.last_used_index += 1
        return "Value successfully inserted"

    def postorder_traversal(self, index):
        if index > self.last_used_index:
            return "End Program"
        self.postorder_traversal(index * 2)
        self.postorder_traversal(index * 2 + 1)
        print(self.custom_list[index])


newBT = BinaryTree(8)
print(newBT.insert_node("Drinks"))
print(newBT.insert_node("Hot"))
print(newBT.insert_node("Cold"))
print(newBT.insert_node("Tea"))
print(newBT.insert_node("Coffee"))
newBT.postorder_traversal(1)
