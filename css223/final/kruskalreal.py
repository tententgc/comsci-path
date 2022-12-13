from typing import List, Tuple


def kruskal(matrix: List[List[int]]) -> List[Tuple[int, int, int]]:
    # Initialize the list of edges and the set of vertices
    edges = []
    vertices = set()

    # Iterate over the matrix to extract the edges and vertices
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # If the edge exists, add it to the list of edges
            if matrix[i][j] > 0:
                edges.append((i, j, matrix[i][j]))

            # Add the vertex to the set of vertices
            vertices.add(i)
            vertices.add(j)

    # Sort the edges in increasing order by weight
    edges.sort(key=lambda edge: edge[2])

    # Initialize the list of connected components
    components = []
    for vertex in vertices:
        components.append([vertex])

    # Initialize the list of edges in the minimum spanning tree
    mst = []

    # Iterate over the edges
    for edge in edges:
        # Find the connected components containing the two vertices
        component1 = None
        component2 = None
        for component in components:
            if edge[0] in component:
                component1 = component
            if edge[1] in component:
                component2 = component

        # If the two vertices are in different connected components, merge them
        if component1 != component2:
            mst.append(edge)
            components.remove(component1)
            components.remove(component2)
            components.append(component1 + component2)

    return mst


# Test the function
matrix = [[0,1,0,4,3,0],
          [1,0,0,4,2,0],
          [0,0,0,0,4,5],
          [4,4,0,0,4,0],
          [3,2,4,4,0,7],
          [0,0,5,0,7,0]]

x = kruskal(matrix)
dis = 0
for i in x: 
    print(i[0],'->',i[1],'=',i[2])
    dis+= i[2]
print("distance =",dis)

    