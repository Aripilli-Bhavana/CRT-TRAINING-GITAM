#if node 14 has a right child, delete it
from collections import deque
def delete_bst(root, key):
    if root is None:
        return root
        # If the tree is empty, return None 
    if key < root.data:
        root.left = delete_bst(root.left, key)
    elif key > root.data:
        root.right = delete_bst(root.right, key)
    else:
        # Node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # Node with two children: Get the in order successor
        temp = root.right
        while temp.left:
            temp = temp.left
        root.data = temp.data
        root.right = delete_bst(root.right, temp.data)
    return root


