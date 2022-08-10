# Create Head and Tail and initialize with Null.
# Then create a blank node and assign a value to it and reference to null
# Link head and tail with these nodes.
class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


singly_linked_list = SLinkedList()
node1 = Node(1)
node2 = Node(2)
singly_linked_list.head = node1
singly_linked_list.head.next = node2
singly_linked_list.tail = node2
