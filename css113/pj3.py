# Prim's Algorithm in Python

INF = 9999999
# number of vertices in graph
N = 5
# creating graph by adjacency matrix method
    # 0  1   2  3  4
G = [[0, 19, 5, 0, 0],  #0
     [19, 0, 5, 9, 2],  #1
     [5, 5, 0, 1, 6],   #2
     [0, 9, 1, 0, 1],   #3
     [0, 2, 6, 1, 0]]   #4


#prim algorithm find way is shortest
selected_node = [0, 0, 0, 0, 0] # selected_node[i] will true if vertex i is included in MST

no_edge = 0

selected_node[0] = True

# printing for edge and weight
print("Edge : Weight\n")
while (no_edge < N - 1):

    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):
                    # not in selected and there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1