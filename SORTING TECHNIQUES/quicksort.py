def qs(l): 
    if(len(l) <= 1):
        return l
    else:
        pi.pop()
        left =[]
        right =[]
        for p in l:
            if(p<pi):
                left.append(p)
            else:
                right.append(p)
    d=qs(left) + [pi] + qs(right)  #[1,5,2,6]+7+[9]====>[1,5,2]+[6]+[7]+[9]
    #[1]+[2]+[5]+[6]+[7]+[9]
    return d

l = list(map(int, input("Enter numbers: ").split()))
print("Before sort:", l)
s=qs(l)
print("After sort:", s)