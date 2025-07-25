#dfs

graph={'0':['1','2'],'1':['0','2','3'],'2':['0','1','4'],'3':['1','4'],'4':['2','3']}
visited=[]
stack=[]
def dfs(node):
    visited.append(node)
    stack.append(node)
    while(stack):
        m=stack.pop()
        print(m,end=" ")#0 2 4 3 1
        for p in graph[m]:
            if p not in visited:
                visited.append(p)
                stack.append(p)
            
dfs('0')