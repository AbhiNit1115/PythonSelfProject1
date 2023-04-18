# Left Subtree --> Root Node --> Right Subtree

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


newBT = TreeNode("Drinks")
left_child = TreeNode("Hot")
right_child = TreeNode("Cold")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
left_child.left_child = tea
left_child.right_child = coffee
newBT.left_child = left_child
newBT.right_child = right_child


def inorder_traversal(root_node):
    if not root_node:
        return
    inorder_traversal(root_node.left_child)
    print(root_node.data)
    inorder_traversal(root_node.right_child)


inorder_traversal(newBT)


class BT:

    def __init__(self, size):
        self.size = size
        self.custom_list = size * [None]
        self.last_used_index = 0
        self.max_size = size

    def insert_bt(self, value):
        if self.last_used_index + 1 == self.max_size:
            return "BT is full"
        self.custom_list[self.last_used_index + 1] = value
        self.last_used_index += 1
        return "Value inserted successfully"

    def search_bt(self, node_value):
        for i in range(len(self.custom_list)):
            if self.custom_list[i] == node_value:
                return "Success"
            else:
                return "Failure"

bt = BT(8)

print(bt.insert_bt("Drinks"))
print(bt.insert_bt("Hot"))
print(bt.insert_bt("Cold"))
print(bt.search_bt(2))

