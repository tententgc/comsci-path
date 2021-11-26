def prim(graph, start):
    mst = set()
    visited = {start}
    nodes, edges = graph

    while len(visited) != len(nodes):
        possible_edges = (e for e in edges if e[0] in visited and e[1] not in visited)
        cheapest_edge = min(possible_edges, key=lambda x: x[2])
        mst.add(cheapest_edge)
        visited.add(cheapest_edge[1])

    return mst
