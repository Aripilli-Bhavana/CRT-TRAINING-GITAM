#iterator will only return the value and enumerator will return the value and the count 
l=[1,2,3,4,5]
r=iter(l)
d1=next(r)
print(d1)


l=[10,20,30,40,50]
r=enumerate(l)
next(r)
r=enumerate(1,5)
next(r)
