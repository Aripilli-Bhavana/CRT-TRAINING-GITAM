nodes=[]
graph=[]
def add_node(node):
    global nc
    if node not in nodes:
         nodes.append(node)
         nc+=1
         graph.append([0]*nc)
    else:
         print("Node already exist")

def add_edge(edge1,edge2): #'A','B'
     index1=nodes.index(edge1) #0
     index2=nodes.index(edge2) #1
     graph[index1][index2]=1
     graph[index2][index1]=1

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
