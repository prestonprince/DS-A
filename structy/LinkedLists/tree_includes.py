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

#! iterative breadth-first
def tree_includes(root, target):
    if not root:
        return False

    queue = deque([ root ])
    
    while queue:
        node = queue.popleft()

        if node.val == target:
            return True

        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)

    return False


#! iterative depth-first
# def tree_includes(root, target):
#     if not root:
#         return False

#     stack = [ root ]

#     while stack:
#         node = stack.pop()

#         if node.val == target:
#             return True

#         if node.right: 
#             stack.append(node.right)

#         if node.left: 
#             stack.append(node.left)
    
#     return False


#! recursive depth-first
# def tree_includes(root, target):
#     if not root:
#         return False

#     if root.val == target:
#         return True

#     return tree_includes(root.left, target) or tree_includes(root.right, target) 


print('TRUE', tree_includes(a, 'e')) 
print('FALSE', tree_includes(a, 'x')) 
