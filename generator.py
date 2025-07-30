#if we want to return multiple values at the same time then we will use generators
#it internally uses yield and next methods

def gen():
    '''
    yield 10
    yield 20
    yield 30
    yield 40
    '''
    l=[10,20,30,40]
    for p in l:
        yield p

g=gen()
'''
r=next(g)
r1=next(g)
r3=next(g)
r4=next(g)
print(r,r1,r3,r4)
'''
for p in q:
    print(p)