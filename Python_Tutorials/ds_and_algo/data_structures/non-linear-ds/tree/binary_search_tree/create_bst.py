# BST: In the left subtree the value of a node is less than or equal to its parent nodes value.
# In the right subtree the value of a node is greater than equal to its parent nodes value.

class BSTNode:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


bst = BSTNode()
