class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            # Node with only one child or no child
            if self.left is None:
                temp = self.right
                return temp
            elif self.right is None:
                temp = self.left
                return temp
            # Node with two children: Get the inorder successor
            temp = self.right
            while temp.left:
                temp = temp.left
            self.data = temp.data
            self.right = self.right.delete(temp.data)
        return self