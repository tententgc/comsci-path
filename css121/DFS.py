def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end: #if start is the same as end, then we have found a path
        return [path]
    paths = []
    for node in graph[start]: #loop dict in graph
        if node not in path:
            # print("node" , node)
            paths.extend(find_all_paths(graph, node, end, path))
    # print("before" , paths)
    return paths


G = {1: [2, 3, 4, 6],
     2: [1, 4, 6],
     3: [1, 2],
     4: [1, 2, 3, 5, 6],
     5: [4, 6], 6: [4]}


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E','F','D'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['H'],
    'F': ['H'],
    'G': ['H'],
    'H': []
}

# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E', 'A', 'H'],
#     'C': ['F', 'G'],
#     'D': ['F'],
#     'E': ['H'],
#     'F': ['H'],
#     'G': ['H'],
#     'H': ['A']
# }

a,b =input().split()
q = find_all_paths(graph,a,b)
x = 1
for i in q:
    print(f'{x:2} ways  = ', *(i))
    x += 1
