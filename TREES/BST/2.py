class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))
    '''else:
        lh = height(root.left)
        rh = height(root.right)
        return max(lh, rh) + 1'''
def inorder(root):
    if(root):
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

n1= Node(27)
n1.insert(14)
n1.insert(35)   
n1.insert(10)
n1.insert(19)
n1.insert(31)
n1.insert(42)
inorder(n1)
h=height(n1)
print("\nHeight of the tree is:", h)  