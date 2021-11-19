
# graph = {
#     'a': {'b': 3, 'c': 4, 'd': 7},
#     'b': {'c': 1, 'f': 5},
#     'c': {'f': 6, 'd': 2},
#     'd': {'e': 3, 'g': 6},
#     'e': {'g': 3, 'h': 4},
#     'f': {'e': 1, 'h': 8},
#     'g': {'h': 2},
#     'h': {'g': 2}
# }

# graph = {
#     'A': {'B': 5, 'E': 1},
#     'B': {},
#     'C': {'D':6},
#     'D': {},
#     'E': {'C':2}
# }

# graph = {
#     'a': {'p1':6, 'p2':3},
#     'p1': {'p2':2, 'p3':2 , 'p4':1,'a':6},
#     'p2': {'p1':2, 'p3':2, 'p4':4, 'a':3},
#     'p3': {'p1':2, 'p2':2, 'p4':2, 'p5':3,'p6':5},
#     'p4':{'p2':4, 'p3':2, 'p5':1, 'p6':4, 'p1':1},
#     'p5':{'p3':3, 'p4':1, 'p6':2,'z':6},
#     'p6':{'p3':5, 'p4':4, 'p5':2, 'z':3},
#     'z':{'p5':6, 'p6':3}
# }

graph = { 
     'a': {'b':1, 'c': 2, 'd': 3},
     'b':{'a':1,'c':5,'b':3},
     'c':{'a':2,'b':5,'d':5,'e':5,'f':2,'g':4},
     'd':{'a':3,'c':5,'g':4},
     'e':{'b':3,'c':5,'f':3,'h':2},
     'f':{'c':2,'e':3,'g':4,'h':1},
     'g':{'c':4,'d':4,'f':4,'h':2},
     'h':{'e':2,'f':1,'g':2,"i":5,'j':5,'k':3},
     'i':{'h':5,'k':4},
     'j':{'h':5,'k':3},
     'k':{'h':3,'i':4,'j':3}
}




def dijkstra(graph, start, goal): 
    shortest_distance = {} #creating a dictionary to store shortest distance
    track_predecessor = {} 
    unseenNodes = graph
    infinity = 9999999
    track_path= []
    path = []

    for node in unseenNodes:
        shortest_distance[node] = infinity 
        shortest_distance[start] = 0
    
    while unseenNodes:
        min_distance_node = None
        
        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node 
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node
        
        path_options = graph[min_distance_node].items()

        for child_node, weight in path_options:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node

        unseenNodes.pop(min_distance_node)
    currentNode = goal
    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    
    track_path.insert(0, start) 

    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('Path is ' + str(track_path))
dijkstra(graph, 'a', 'i')
