
# Doubly Linked List (DLL)


class DoublyLinkedList:
    def __init__(self, nodes=None):
        self.head = None
        
        if nodes is not None:
            node = Node(value=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(value=elem)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return self.value