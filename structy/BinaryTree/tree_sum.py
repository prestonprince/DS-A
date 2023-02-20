from collections import deque

class Node: 
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


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

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

#! iterative breadth-first
def tree_sum(root):
    if not root: 
        return 0

    queue = deque([ root ])
    sum = 0

    while queue:
        node = queue.popleft()
        sum += node.val

        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    
    return sum

#! iterative depth-first
# def tree_sum(root):
#     if not root:
#         return 0

#     sum = 0
#     stack = [ root ]

#     while stack:
#         node = stack.pop()
#         sum += node.val

#         if node.right: stack.append(node.right)
#         if node.left: stack.append(node.left)

#     return sum

#! recursive depth-first
# def tree_sum(root, sum = 0):
#     if not root:
#         return 0

#     return root.val + tree_sum(root.left) + tree_sum(root.right)

print(tree_sum(a)) # -> 21
