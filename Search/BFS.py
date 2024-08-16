
# Breadth First Search
# O(n)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
        
    def BFS(self, target_value):
        q = [self.root]

        while len(q):
            next = q.pop()
            if next.value == target_value:
                return True
            
            if next.left:
                q.append(next.left)

            if next.right:
                q.append(next.right)

        return False





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

print(tree.BFS(3))
