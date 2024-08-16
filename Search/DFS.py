
# Depth First Search
# 

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


visited = set()
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    # def DFS(self, node, traversal, target_value):
    #     if node not in visited:
    #         print(node)
    #         visited.add(node)
    #         DFS()





tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

#              1
#           /     \
#          2       3
#        /  \     /  \
#       4    5   6    7

print(tree.DFS(tree.root, "", 5))
