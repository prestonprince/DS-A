# Write a function, create_linked_list, that takes in a list of values as an argument. 
# The function should create a linked list containing each item of the list as the values of the nodes. 
# The function should return the head of the linked list.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def create_linked_list(values):
    dummy = Node(None)
    tail = dummy

    for val in values:
        tail.next = Node(val)
        tail = tail.next
    return dummy.next

print(create_linked_list(["h", "e", "y"]))
# h -> e -> y
