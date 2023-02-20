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

def path_finder(root, target):
    res = _path_finder(root, target)

    return res[::-1] if res is not None else None

def _path_finder(root, target):
    if not root:
        return None

    if root.val == target:
        return [ root.val ]

    left_path = _path_finder(root.left, target)
    if left_path is not None:
        left_path.append(root.val)
        return left_path

    right_path = _path_finder(root.right, target)
    if right_path is not None:
        right_path.append(root.val)
        return right_path

    return None


print(path_finder(a, 'e'))
