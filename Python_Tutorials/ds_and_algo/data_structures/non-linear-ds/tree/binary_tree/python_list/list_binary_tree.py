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

    def search_node(self, node_value):
        for i in range(len(self.custom_list)):
            if self.custom_list[i] == node_value:
                return "Success"
            else:
                return "Not Found"


newBT = BinaryTree(8)
print(newBT.insert_node("Drinks"))
print(newBT.insert_node("Hot"))
print(newBT.insert_node("Cold"))
print(newBT.search_node("Cold"))

