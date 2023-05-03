graph = {
  'a' : ['b','c','d'],
  'b' : ['a','c', 'd'],
  'c' : ['a','b','e'],
  'd' : ['a','b','e','f'],
  'e' : ['c','d','f'],
  'f' : ['d','e']
}
visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs
    if node not in visited:
        print (node)
        visited.add(node)
        for i in graph[node]:
            dfs(visited, graph, i)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, 'a')
