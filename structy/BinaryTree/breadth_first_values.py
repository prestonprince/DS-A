from collections import deque

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

def breadth_first_values(root):
    if not root: return []

    values = []
    queue = deque([ root ])

    while queue:
        node = queue.popleft()
        values.append(node.val)

        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)

    return values


print('breadth',breadth_first_values(a))
