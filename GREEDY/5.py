def knapsack(v,w,c):
    ratio=[v[p]/w[p],w[p],v[p] for p in range(len(v))]
    ratio.sort(reverse=True)
    mv=0
    for ra in ratio:
        r,w,v=ra
        if(c>=w):
            c-=w
            mv+=v
        else:
            d=c/wmv=mv+(d*w)
    return mv

val=[60,100,120]
wt=[10,20,30]
c=50
k=knapsack(val,wt,c)
print("Maximum value in Knapsack =", k) 
