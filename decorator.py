def dist(d):
    def new_display():
        print("************")
        d()
        print("************")
    return new_display

@dis
def display():
    print("Python Programming")
display()



def division(d):
    def new_division(a,b):
        if b==0:
            return 0
        else:
            return d(a,b)
    return new_division

@division
def div(a,b):
    return a/b
d=div(10,2)
print(d)
d=div(10,0)
print(d)

        