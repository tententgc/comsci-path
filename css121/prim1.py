#prim's algorithm

graph = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]
def primalgorithm(graph):
    #graph = [[0, 19, 5, 0, 0],
    #     [19, 0, 5, 9, 2],
    #     [5, 5, 0, 1, 6],
    #     [0, 9, 1, 0, 1],
    #     [0, 2, 6, 1, 0]]
    n = len(graph)
    visited = [False] * n
    visited[0] = True
    mincost = 0
    path = []
    for i in range(n-1):
        mincost = 10000000
        for j in range(n):
            if not visited[j]:
                if graph[i][j] < mincost:
                    mincost = graph[i][j]
                    minindex = j
        visited[minindex] = True
        for k in range(n):
            if graph[minindex][k] < graph[minindex][i]:
                graph[minindex][i] = graph[minindex][k]
        path.append([minindex, i])
        print(graph)
    return path


print(primalgorithm(graph))
