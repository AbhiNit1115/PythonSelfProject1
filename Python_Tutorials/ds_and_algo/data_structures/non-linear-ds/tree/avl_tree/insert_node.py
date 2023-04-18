# for insertion a node in AVL we need 2 cond: rotation is not required its same as inserting a node in BT
# Rotation is required: these are of 4 types
# LL cond: First find the disbalanced node Any time we face LL cond we have to perform right rotation.
class AVL:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1


def rotate_child(disbalanced_node):
    new_root = disbalanced_node.left_child
    disbalanced_node.left_child = disbalanced_node.left_child.right_child
    new_root.right_child = disbalanced_node
    return new_root
