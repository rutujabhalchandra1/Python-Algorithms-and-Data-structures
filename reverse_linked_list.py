class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None

def reverse_list(head):
    current = head
    prev = None
    nextnode = None

    while current:
        nextnode = current.nextnode
        current.nextnode = prev
        prev = current
        current = nextnode
    return prev

a = Node(1)
b = Node(2)
c = Node(3)
a.nextnode = b
b.nextnode = c
print(a.nextnode.value)
print(b.nextnode.value)
reverse_list(a)
print(a.nextnode.value)
print(b.nextnode.value)