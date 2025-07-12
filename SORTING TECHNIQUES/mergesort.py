def merged(left, right): #30 40 60 --- 10 20 50 
    i=0
    j=0
    m=[]
    while(i<len(left)) and (j<len(right)):
        if(left[i]<right[j]): #30<10
            m.append(left[i]) #m=[10]
            i+=1
        else:
            m.append(right[j]) #m=[10,20]
            j+=1    
    d=m+left[i:]+right[j:] #m=[10,20,30,40,50,60]
    return d
def merge(l):
    if(len(l)==1):
        return l
    else:
        m=len(l)//2
        left=merge(l[:m]) #[:3] #60 40 30#60 40 30#60 40 30 #30 40 60
        right=merge(l[m:]) #l[3:] #50 20 10#50 20 10#50 20 10 #10 20 50
        return merged(left, right)
    
    l=[60, 40, 30, 50, 20, 10]
    print("Before sort:",l)
    m=merge(l)
    print("After sort:",m)