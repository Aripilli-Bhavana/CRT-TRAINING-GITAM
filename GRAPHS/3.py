nodes=[]
graph=[]
def add_node(node):
    global nc
    if node not in nodes:
         nodes.append(node)
         nc+=1
         graph.append([0]*nc)
         for i in graph:
             i.append(0)
    else:
         print("Node already exist")

def add_edge(edge1,edge2,val): #'A','B'
     index1=nodes.index(edge1) #0
     index2=nodes.index(edge2) #1
     graph[index1][index2]=val
     graph[index2][index1]=val

def print_matrix(nc):
     for p in range(nc):
        for q in range(nc):
            print(graph[p][q], end=" ")
        print()

nc=0
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')
add_node('F')
add_node('A')
add_edge('A','B',3)
add_edge('A','C',5)
add_edge('A','D',2)
add_edge('B','D',4)
add_edge('B','E',6)
add_edge('C','D',3)
add_edge('D','E',1)
add_edge('E','F',3)

print(nodes)
print_matrix(nc)