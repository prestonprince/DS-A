# Write a function, has_path, that takes in a dictionary representing the 
# adjacency list of a directed acyclic graph and two nodes (src, dst). The function should 
# return a boolean indicating whether or not there exists a directed path between the source and destination nodes.

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

#! depth first
def has_path(graph, src, dst):
  stack = [ src ]
  
  while stack:
    current = stack[-1]
    if current == dst:
      return True
    stack.pop()
    for neighbor in graph[current]:
      stack.append(neighbor)
  return False

from collections import deque

#! breadth first
# def has_path(graph, src, dst):
#   q = deque([ src ])
  
#   while q:
#     current = q[0]
#     if current == dst:
#       return True
#     q.popleft()
#     for neighbor in graph[current]:
#       q.append(neighbor)
#   return False

#! depth first recursive
def has_path(graph, src, dst):
  if src == dst:
    return True
  
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst) == True:
      return True
  return False

print(has_path(graph, 'f', 'k')) # True
