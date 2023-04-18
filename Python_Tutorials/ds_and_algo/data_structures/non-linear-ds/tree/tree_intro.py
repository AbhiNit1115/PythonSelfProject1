# A tree is a non-linear DS with hierarchical relationships between its elements w/o having any cycle,
# its basically reversed from a real life tree.

class TreeNode:

    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = "  " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

