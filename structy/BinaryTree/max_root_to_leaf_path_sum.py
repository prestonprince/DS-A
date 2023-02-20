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

def max_path_sum(root):
    if not root:
        return float('-inf')

    left_path = max_path_sum(root.left)
    right_path = max_path_sum(root.right)

    if not root.right and not root.left:
        return root.val

    return root.val + max(left_path, right_path)


print(max_path_sum(a)) # -> 18
