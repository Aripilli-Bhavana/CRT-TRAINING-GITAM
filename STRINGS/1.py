#implement the following function: def frequent_character_replaced(string,x):
s= input()#liril
x=input()#t
d={}#{'l': 2, 'i': 1, 'r': 2}
for p in s:
    if p not in d:
        d[p]=1
    else:
        d[p]+=1
m=max(d.values())#2
l=[]
for p,q in d.items():
    if q==m:
        l.append(p)
l.sort()#['i','l']
r=''#ltrtl
for p in s:
    if (p==l[0]):
        r+=x
print(r)