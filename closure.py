def power(n): #5
    def pow(p): 
        return n**p
    return pow
r=power(5)
d=r(3)
r1=power(5)
d1=r1(3)
print(d1)
