#write a program to implement level order using deque
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
    def zigzag_q(root):
        if root is None:
            return 0
        r=[] #[[27],[35,14],[10,19,31,42],[50]]
        q=deque([root])
        lr=True
        while q: #1
            level_size = len(q) #3
            level_nodes = deque()
            for p in range(level_size):
                node = q.popleft()
                if lr:
                    level_nodes.append(node.data) #deque ([10,19,31,42])
                else:
                    level_nodes.appendleft(node.data)#[35,14]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)#150
            lr=not lr#false
            r.append(list(level_nodes))
        return r