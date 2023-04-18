# Left Subtree --> Right Subtree --> Root Node

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
nonalc = TreeNode("Non-Alcoholic")
alc = TreeNode("Alcoholic")
left_child.left_child = tea
left_child.right_child = coffee
right_child.right_child = alc
right_child.left_child = nonalc
newBT.left_child = left_child
newBT.right_child = right_child


def postorder_traversal(root_node):
    if not root_node:
        return
    postorder_traversal(root_node.left_child)
    postorder_traversal(root_node.right_child)
    print(root_node.data)


postorder_traversal(newBT)
