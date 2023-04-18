# Here we traverse the tree level by level first root node then second level (left to right) then third
# and so on

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

    def level_order_traversal(self, index):
        if index > self.last_used_index:
            return "End Program"
        for i in range(index, self.last_used_index + 1):
            print(self.custom_list[i])

    def delete_node(self, value):
        if self.last_used_index == 0:
            return "No node to delete"
        for i in range(1, self.last_used_index+1):
            if self.custom_list == value:
                self.custom_list[i] = self.custom_list[self.last_used_index]
                self.custom_list[self.last_used_index] = None
                self.last_used_index -= 1
                return "Node is successfully deleted"


newBT = BinaryTree(8)
print(newBT.insert_node("Drinks"))
print(newBT.insert_node("Hot"))
print(newBT.insert_node("Cold"))
print(newBT.insert_node("Tea"))
print(newBT.insert_node("Coffee"))
print(newBT.delete_node("Tea"))
print(newBT.level_order_traversal(1))
