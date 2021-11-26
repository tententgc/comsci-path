graph = {
    'a': {'b': 1, 'c': 2, 'd': 3},
    'b': {'a': 1, 'c': 5, 'e': 3},
    'c': {'a': 2, 'b': 5, 'd': 5, 'e': 5, 'f': 2, 'g': 4},
    'd': {'a': 3, 'c': 5, 'g': 4},
    'e': {'b': 3, 'c': 5, 'f': 3, 'h': 2},
    'f': {'c': 2, 'e': 3, 'g': 4, 'h': 1},
    'g': {'c': 4, 'd': 4, 'f': 4, 'h': 2},
    'h': {'e': 2, 'f': 1, 'g': 2, "i": 5, 'j': 5, 'k': 3},
    'i': {'h': 5, 'k': 4},
    'j': {'h': 5, 'k': 3},
    'k': {'h': 3, 'i': 4, 'j': 3}
}

start, stop = input().split()


def find_min_paths(start, stop, graph, now=start, path=start, dis=0, min_dis=float('inf'), min_path=""):
    if now == stop:
        return dis, path

    if now in path[:-1]:
        return float("inf"), ""

    for i in graph[now]:
        min_, path_ = find_min_paths(
            start, stop, graph, i, path+i, dis+graph[now][i], min_dis, min_path)
        if min_ < min_dis:
            min_path = path_
            min_dis = min_

    return min_dis, min_path


print(find_min_paths(start, stop, graph))
