def dist(d):
    def new_display():
        print("************")
        d()
    return new_display

@dis
def display():
    print("Python Programming")
display()
