



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported")
            return False

    def preorder_print(self, start, traversal):
        # Preorder traversal: Root -> Left -> Right
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        # In-order traversal: Left -> Root -> Right
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)                      
        return traversal
    
    def postorder_print(self, start, traversal):
        # Post-order traversal: Left -> Right -> Root
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal



tree1 = BinaryTree(1)
tree1.root.left = Node(2)
tree1.root.right = Node(3)
tree1.root.left.left = Node(4)
tree1.root.left.right = Node(5)
tree1.root.right.left = Node(6)
tree1.root.right.right = Node(7)

#              1
#           /     \
#          2       3
#        /  \     /  \
#       4    5   6    7


tree2 = BinaryTree(1)
tree2.root.left = Node(2)
tree2.root.left.left = Node(4)
tree2.root.left.right = Node(5)


#              1
#           / 
#          2   
#        /  \     
#       4    5   

# pre-order: 1-2-4-5
# in-order: 4-2-5-1
# post-order: 4-5-2-1

print(tree2.print_tree("preorder"))
