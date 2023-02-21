class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

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

def tree_levels(root):
    if not root: return []

    levels = []
    stack = [ (root, 0) ]

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

    return levels

print(tree_levels(a)) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f']
# ]
