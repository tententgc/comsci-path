def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            paths.extend(find_all_paths(graph, node, end, path))
    return paths

G = {1:[2,3,4,6], 2:[1,4,6], 3:[1,2], 4:[1,2,3,5,6], 5:[4,6],6:[4] }
print(find_all_paths(G, 1, 6))