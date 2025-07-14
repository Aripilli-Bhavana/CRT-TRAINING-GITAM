def level(root)
    h=height(root) #3
    for p in range(1,h+1):
        current(root,p) #(root,3)
def current(root, l): #(root,1)
    if root is None:
        return 0
    elif(l==1):
        print(root.data, end=' ') #27 14 35 10 19 31 42
    else:
        current(root.left, l-1) #current(50, 2) #current(25,1) #current(125,1)
        current(root.right, l-1) #current(150, 2) #current(75,1) #current(180,1)
n1= Nodee(27)
n1.insert(14)
n1.insert(35)   
n1.insert(10)
n1.insert(19)
n1.insert(31)
n1.insert(42)
inorder(n1)
h=height(n1)
print("\nHeight of the tree is:", h)    
print("\nLevel order traversal is:")
level(n1) #27 14 35 10 19 31 42