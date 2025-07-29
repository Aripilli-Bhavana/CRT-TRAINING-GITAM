def mindistance(V, dist, visited):
    min_val = 9999
    min_index = -1
    for v in range(V):
        if dist[v] < min_val and visited[v] == False:
            min_val = dist[v]
            min_index = v
    return min_index

def dijkstra(graph, V, src):
    dist = [9999] * V
    dist[src] = 0
    visited = [False] * V

    for count in range(V):
        u = mindistance(V, dist, visited)
        visited[u] = True

        for v in range(V):
            if graph[u][v] > 0 and not visited[v] and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]

    print("Vertex\tDistance from Source")
    for node in range(V):
        print(node, "\t", dist[node])

# ✅ Build adjacency matrix based on given edges
V = 5
graph = [[0 for _ in range(V)] for _ in range(V)]

# Add edges
graph[0][1] = 10
graph[0][2] = 5
graph[2][3] = 7
graph[2][4] = 8
graph[2][1] = 2
graph[1][3] = 1
graph[3][4] = 1

# Run Dijkstra from source 0
dijkstra(graph, V, 0)