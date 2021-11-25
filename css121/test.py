import heapq
import sys


class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name, edges):
        self.vertices[name] = edges

    def shortest_path(self, start, finish):
        distances = {}  # Distance from start to node
        previous = {}  # Previous node in optimal path from source
        nodes = []  # Priority queue of all nodes in Graph

        for vertex in self.vertices:
            if vertex == start:  # Set root node as distance of 0
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None

        while nodes:
            # Vertex in nodes with smallest distance in distances
            smallest = heapq.heappop(nodes)[1]
            if smallest == finish:  # If the closest node is our target we're done so print the path
                path = []
                # Traverse through nodes til we reach the root which is 0
                while previous[smallest]:
                    path.append(smallest)
                    smallest = previous[smallest]
                return path
            # All remaining vertices are inaccessible from source
            if distances[smallest] == sys.maxsize:
                break

            # Look at all the nodes that this vertex is attached to
            for neighbor in self.vertices[smallest]:
                # Alternative path distance
                alt = distances[smallest] + self.vertices[smallest][neighbor]
                # If there is a new shortest path update our priority queue (relax)
                if alt < distances[neighbor]:
                    distances[neighbor] = alt
                    previous[neighbor] = smallest
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
        return distances

    def __str__(self):
        return str(self.vertices)


if __name__ == '__main__':
    g = Graph()
    g.add_vertex('A', {'B': 7, 'C': 8})
    g.add_vertex('B', {'A': 7, 'F': 2})
    g.add_vertex('C', {'A': 8, 'F': 6, 'G': 4})
    g.add_vertex('D', {'F': 8})
    g.add_vertex('E', {'H': 1})
    g.add_vertex('F', {'B': 2, 'C': 6, 'D': 8, 'G': 9, 'H': 3})
    g.add_vertex('G', {'C': 4, 'F': 9})
    g.add_vertex('H', {'E': 1, 'F': 3})
    print(g.shortest_path('A', 'H'))
