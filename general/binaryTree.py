# Arboles binarios
# Un árbol binario básico con una función de recorrido en preorden:
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
preorder_traversal(root)  # Output: 1 2 3
