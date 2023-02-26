# Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes 
# (node_A, node_B). The function should return a boolean indicating whether or not there exists a path between node_A and node_B.

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

def build_graph(edges):
  graph = {}
  for a, b in edges:
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    
    graph[a].append(b)
    graph[b].append(a)
  return graph

#! depth first iterative
# def undirected_path(edges, node_A, node_B):
#   graph = build_graph(edges)
#   stack = [ node_A ]
#   visited = set()
  
#   while stack:
#     current = stack[-1]
    
#     if current == node_B:
#       return True
    
#     visited.add(current)
#     stack.pop()
    
#     for neighbor in graph[current]:
#       if neighbor not in visited:
#         stack.append(neighbor)
#   return False

#! depth first recursive
# def undirected_path(edges, node_A, node_B):
#   graph = build_graph(edges)
#   return has_path(graph, node_A, node_B, set())
  

# def has_path(graph, node_A, node_B, visited):
#   if node_A == node_B:
#     return True
  
#   visited.add(node_A)
#   for neighbor in graph[node_A]:
#     if neighbor not in visited:
#       if has_path(graph, neighbor, node_B, visited) == True:
#         return True
#   return False


from collections import deque
#! breadth first
def undirected_path(edges, node_A, node_B):
  graph = build_graph(edges)
  q = deque([ node_A ])
  visited = set()
  
  while q:
    current = q[0]
    if current == node_B:
      return True
    visited.add(current)
    q.popleft()
    
    for neighbor in graph[current]:
      if neighbor not in visited:
        q.append(neighbor)
  return False

print(undirected_path(edges, 'j', 'm')) # -> True
