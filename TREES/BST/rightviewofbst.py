#right view of bst
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
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
'''
def right_view(root):
    if not root:
        return 0
    q = deque([queue])
    q.append(root)
    while q:
        n = len(q)
        for i in range(n):
            node = q.popleft()
            # print the rightmost element at the current level
            if i == n - 1:
                print(node.data, end=' ')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
'''


def right_view(root):
    if root is None:
        return 0
    q=deque([root])#180
    while(q):
        n = len(q)#4
        for p in range(n):
            node=q.popleft()#180
            if(p==n-1):
                print(node.data, end=' ')#27 35 42
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

def left_view(root):
    if root is None:
        return 0
    q=deque([root])
    while(q):
        n = len(q)
        for p in range(n):
            node=q.popleft()
            if(p==0):
                print(node.data, end=' ')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


# Example usage:
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print("Right view of BST:")
right_view(root)

print("\nLeft view of BST:")
left_view(root)
    