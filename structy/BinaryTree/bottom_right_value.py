class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

a = Node(3)
b = Node(11)
c = Node(10)
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
#   11     10
#  / \      \
# 4   -2     1

from collections import deque

def bottom_right_value(root):
    queue = deque([ root ])
    curr = None

    while queue:
        curr = queue.popleft()

        if curr.left:
            queue.append(curr.left)
        
        if curr.right:
            queue.append(curr.right)

    return curr.val

print(bottom_right_value(a)) # -> 1
