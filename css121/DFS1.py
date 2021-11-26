 

# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E','A','H'],
#     'C': ['F', 'G'],
#     'D': ['F'],
#     'E': ['H'],
#     'F': ['H'],
#     'G': ['H'],
#     'H': ['A']
# }


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F', 'D'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['H'],
    'F': ['H'],
    'G': ['H'],
    'H': []
}
start,stop = input().split()
count =  0

def find_path(start,stop,graph, now = start , path = start):
    global count
    if path.count(now) > 1 : 
        return
    if now == stop:
        count += 1
        print('ways = ', count , ":" ,*[i for i in path]) 
        return
    for i in graph[now]:
        find_path(start,stop,graph,i,path+i)
find_path(start,stop,graph)
