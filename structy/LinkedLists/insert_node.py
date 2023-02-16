# Write a function, insert_node, that takes in the head of a linked list, a value, and an index. 
# The function should insert a new node with the value into the list at the specified index. Consider the head 
# of the linked list as index 0. The function should return the head of the resulting linked list.

# Do this in-place.

# You may assume that the input list is non-empty and the index is not greater than the length of the input list.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

def insert_node(head, value, index):
    new_node = Node(value)

    if index == 0:
        new_node.next = head
        return new_node

    i = 0
    current = head

    while current:
        if i == index-1:
            next = current.next
            current.next = new_node
            new_node.next = next
            break

        i+=1
        current = current.next
        
    return head



print(insert_node(a, 'x', 2))
# a -> b -> x -> c -> d
