class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   6     6
#  / \     \
# 4   6     12

from collections import deque

#! depth first iterative
def tree_value_count(root, target):
  if not root:
    return 0
  
  count = 0
  stack = [ root ]
  
  while stack:
    current = stack.pop()
    
    if current.val == target:
      count += 1
      
    if current.right:
      stack.append(current.right)
      
    if current.left:
      stack.append(current.left)
  return count


#! breadth first iterative
# def tree_value_count(root, target):
#   if not root:
#     return 0
  
#   count = 0
#   queue = deque([ root ])
  
#   while queue:
#     current = queue.popleft()
    
#     if current.val == target:
#       count += 1
    
#     if current.left:
#       queue.append(current.left)
    
#     if current.right:
#       queue.append(current.right)
      
#   return count


#! depth first recursive
# def tree_value_count(root, target):
#   if not root:
#     return 0
  
#   count = 1 if root.val == target else 0
  
#   left_count = tree_value_count(root.left, target)
#   right_count = tree_value_count(root.right, target)
  
#   return count + left_count + right_count

print(tree_value_count(a,  6)) # -> 3
