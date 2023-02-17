# Write a function, depth_first_values, that takes in the root of a binary tree. 
# The function should return a list containing all values of the tree in depth-first order.

class Node: 
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')        
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f


#! iterative
def depth_first_values(root):
  if not root: return []
  stack = [root]
  res = []
  
  while len(stack):
    current = stack.pop()
    
    # do the thing!
    res.append(current.val)
    
    if current.right: stack.append(current.right)
    if current.left: stack.append(current.left)
  return res


#! recursive
# def depth_first_values(root):
#   if not root:
#     return []
  
#   left_values = depth_first_values(root.left)
#   right_values = depth_first_values(root.right)
#   return [ root.val, *left_values, *right_values ]

print(depth_first_values(a))
#   -> ['a', 'b', 'd', 'e', 'c', 'f']
