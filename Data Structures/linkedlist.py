
# Linked list 


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0)) # getting the data for the head
            self.head = node # initiating the head
            for elem in nodes:
                node.next = Node(data=elem)  # adding a new node with the element from nodes
                node = node.next # "moving to right"

    # To represent the linked list
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next 
        nodes.append('None')
        return " -> ".join(nodes)
    
    # to traverse the list
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node 
            node = node.next

    def add_first(self, node):
        # define the position of the new node (before the head)
        node.next = self.head
        # bring the head to the new first element
        self.head = node

    def add_last(self, node):
        # if we dont have a linked list yet we create the head element
        if self.head is None:
            self.head = node
            return
        # pass through all the elements
        for current_node in self:
            pass
        # now at the last element current.node (the tail)
        tail = current_node
        tail.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("The list is empty")

        # passing through all the nodes
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with data '%s' not found" % target_node_data)
    
        
    def remove_node(self, target_node_data):
        # check if list is empty
        if self.head is None:
            raise Exception('List is empty')
        
        # remove the head
        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        # save the previous node
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node
        
        raise Exception("Node with data '%s' not found" % target_node_data )
                


# Class for the indiviual node [node.data, node.next]
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
    


# add_first, add_last, add_after, remove_node

llist = LinkedList(['a', 'b', 'c'])
llist.remove_node('b')
print(repr(llist))