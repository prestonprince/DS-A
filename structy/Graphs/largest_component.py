# Write a function, largest_component, that takes in the adjacency list of an undirected graph. 
# The function should return the size of the largest connected component in the graph.

def largest_component(graph):
    max = 0

    for node in graph:
        size = explore(graph, node, set())
        if size > max: 
            max = size
    return max

def explore(graph, current, visited):
    if current in visited:
        return 0

    visited.add(current)

    size = 1
    for neighbor in graph[current]:
        size += explore(graph, neighbor, visited)
    return size

print(largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # -> 4
