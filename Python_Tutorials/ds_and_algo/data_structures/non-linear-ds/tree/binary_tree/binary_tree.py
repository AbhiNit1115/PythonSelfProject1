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


def pre_order_traversal(root_node):
    if not root_node:
        return
    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)


pre_order_traversal(newBT)
print("__________________")


def inorder_traversal(root_node):
    if not root_node:
        return
    pre_order_traversal(root_node.left_child)
    print(root_node.data)
    pre_order_traversal(root_node.right_child)


inorder_traversal(newBT)
print("_______________________")


def postorder_traversal(root_node):
    if not root_node:
        return
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)
    print(root_node.data)


postorder_traversal(newBT)
