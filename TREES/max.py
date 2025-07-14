#find max value in the node

def level_q(root):
    if root is None:
        return 0
    q = deque([root]) #[]
    while q:
        node = q.popleft()
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

n1= Nodee(27)
n1.insert(14)
n1.insert(35)   
n1.insert(10)
n1.insert(19)
n1.insert(31)
n1.insert(42)
inorder(n1)