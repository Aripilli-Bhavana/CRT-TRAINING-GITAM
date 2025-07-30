#generate 4 digit otp number and return to main program using generators in python 

import random
def gen():
    for p in range(3):
        yield random.randint(1000,9999)
g=gen()
'''
r=next(g)
r1=next(g)
r3=next(g)
r4=next(g)
print(r,r1,r3,r4)
'''
for p in g:
    print(p)
