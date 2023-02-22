class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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

def leaf_list(root):
    if root is None:
        return []

    stack = [ root ]
    leaves = []

    while stack:
        current = stack.pop()

        if current.left is None and current.right is None:
            leaves.append(current.val)
        
        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)
    return leaves


print(leaf_list(a)) # -> [ 'd', 'e', 'f' ]
