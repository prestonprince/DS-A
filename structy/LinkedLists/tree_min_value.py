class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(14)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       5
#    /    \
#   11     3
#  / \      \
# 4   14     12

from collections import deque

#! iterative breadth first solution
# def tree_min_value(root):
#   min = float('inf')
  
#   queue = deque([ root ])

#   while queue:
#     node = queue.popleft()
#     if node.val < min:
#       min = node.val

#     if node.left: queue.append(node.left)
#     if node.right: queue.append(node.right)
  
#   return min


#! iterative depth-first solution
def tree_min_value(root):
  min = float('inf')
  
  stack = [ root ]
  
  while stack:
    node = stack.pop()
    if node.val < min:
      min = node.val

    if node.right: stack.append(node.right)
    if node.left: stack.append(node.left)

  return min


#! recursive depth first
def tree_min_value(root):
  if root is None:
    return float("inf")
  smallest_left_value = tree_min_value(root.left)
  smallest_right_value = tree_min_value(root.right)
  return min(root.val, smallest_left_value, smallest_right_value)

tree_min_value(a) # -> 3
