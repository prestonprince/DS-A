# Write a function, connected_components_count, that takes in the adjacency 
# list of an undirected graph. The function should return the number of connected components within the graph.

#! depth first recursive
def connected_components_count(graph):
    visited = set()
    count = 0

    for node in graph:
        if explore(graph, node, visited) == True:
            count+=1
    return count

def explore(graph, current, visited):
    """
    recursively traverse graph, return true for every complete traversal
    return false if node of current call has been visited already
    """
    if current in visited:
        return False
    
    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)

    return True

#! depth first iterative
# def connected_components_count(graph):
#     main_visited = set()
#     count = 0

#     for node in graph:
#         visited = set()
#         if node not in main_visited:
#             stack = [ node ]

#             while stack:
#                 current = stack[-1]

#                 visited.add(current)
#                 main_visited.add(current)
#                 stack.pop()

#                 for neighbor in graph[current]:
#                     if neighbor not in visited:
#                         stack.append(neighbor)
#             count+=1
#     return count

print(connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # -> 2
