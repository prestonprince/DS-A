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

def how_high(root):
    if not root:
        return -1

    left = how_high(root.left)
    right = how_high(root.right)

    return 1 + max(left, right)

print(how_high(a)) # -> 2
