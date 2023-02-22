class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
from statistics import mean

def level_averages(root):
    if not root:
        return []

    stack = [ (root, 0) ]
    levels = []

    while stack:
        current, level = stack.pop()

        if len(levels) == level:
            levels.append([ current.val ])
        else:
            levels[level].append(current.val)

        if current.right:
            stack.append( (current.right, level+1) )
        if current.left:
            stack.append( (current.left, level+1) )

    averages = list(map(lambda x: mean(x), levels))
    return averages

print(level_averages(a)) # -> [ 3, 7.5, 1 ] 
