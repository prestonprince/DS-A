# Write a function, has_cycle, that takes in an object representing the adjacency list of a directed graph. The function should return a 
# boolean indicating whether or not the graph contains a cycle.

def has_cycle(graph):
    visited = set()
    for node in graph:
        if is_cycle(graph, node, set(), visited):
            return True
    return False

def is_cycle(graph, node, visiting, visited):
    if node in visited:
        return False

    if node in visiting:
        return True

    visiting.add(node)

    for neighbor in graph[node]:
        if is_cycle(graph, neighbor, visiting, visited):
            return True
    
    visiting.remove(node)
    visited.remove(node)
    return False

print(has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
})) # -> True
