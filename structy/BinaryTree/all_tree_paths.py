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

def all_tree_paths(root):
    if not root:
        return []

    if not root.right and not root.left:
        return [[ root.val ]]

    paths = []

    left_paths = all_tree_paths(root.left)
    for path in left_paths:
        paths.append([ root.val, *path ])

    right_paths = all_tree_paths(root.right)
    for path in right_paths:
        paths.append([ root.val, *path ])
    
    return paths


print(all_tree_paths(a)) # ->
# [ 
#   [ 'a', 'b', 'd' ], 
#   [ 'a', 'b', 'e' ], 
#   [ 'a', 'c', 'f' ] 
# ] 
