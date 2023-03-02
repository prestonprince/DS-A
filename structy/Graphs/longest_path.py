# Write a function, longest_path, that takes in an adjacency list for a directed acyclic graph. 
# The function should return the length of the longest path within the graph. A path may start and end at any
#  two nodes. The length of a path is considered the number of edges in the path, not the number of nodes.

graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': []
}

def longest_path(graph):
    distance = {}
    for node in graph:
        if len(graph[node]) == 0:
            distance[node] = 0

    for node in graph:
        traverse(graph, node, distance)
    
    return max(distance.values())


def traverse(grid, node, distance):
    if node in distance:
        return distance[node]

    longest = 0
    for neighbor in graph[node]:
        length = traverse(grid, neighbor, distance)
        if length > longest:
            longest = length 

    distance[node] = 1 + longest
    return distance[node]


print(longest_path(graph)) # -> 2
