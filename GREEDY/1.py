#sort according to the length of the string
# This code sorts a list of strings first by their length and then by their first character.

x=["Kiran","Lokesh","Raju","Abc"]
x.sort(key=lambda x: len(x))
print(x)

#sort according to first character
# This code sorts a list of strings by their first character.
x=["Kiran","Lokesh","Raju","Abc"]
x.sort(key=lambda x: x[0])
print(x)

#sort according to the length of the string and then by last character
# This code sorts a list of strings first by their length and then by their last character. 
x=["Kiran","Lokesh","Raju","Abc"]
x.sort(key=lambda x: (len(x), x[-1]))
print(x)

#sort according to the second character, sort according to the last char and print in descending order
l1=['A','B','C','D']
l2=[11,5,3,2]
l=list(zip(l1,l2))
print(l)

#it prints a list of tuples  [('A', 11), ('B', 5), ('C', 3), ('D', 2)]

l.sort(key=lambda x: (x[1]), reverse=True)
print(l)


'''
GREEDY ALGO is basically used for optimization problems where we want to find the best solution according to the constraints given.
'''