#write a program to search 10 in a BST
from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)
def search_bst(root, key):
    result = search(root, key)
    if result:
        print(f"Node with value {key} found in the BST.")
    else:
        print(f"Node with value {key} not found in the BST.")
if __name__ == "__main__":
    root = Node(27)
    root.insert(35)
    root.insert(14)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    root.insert(50)

    
    search_bst(root, 10)  
    search_bst(root, 100) 



    #create, traversal, height, level order, zigzag level order, right view, left view