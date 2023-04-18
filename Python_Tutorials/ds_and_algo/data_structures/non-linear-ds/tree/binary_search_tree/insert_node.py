# Inserting a value in BST:
# - First option is root node is blank meaning the tree is blank this is fairly simple.
# Second option is BST has some nodes in it. In order to insert a node we have to start with the root node and
# traverse towards left or right. If value is smaller than root node value insert left if bigger insert right.
class BSTNode:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


bst = BSTNode()