class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None

def cycle_check(node):
    marker_1 = node
    marker_2 = node

    if marker_2 != None and marker_2.nextnode != None:
        marker_1 = marker_1.nextnode
        marker_2 = marker_2.nextnode.nextnode
        if marker_1 == marker_2:
            return True
    return False
a = Node(1)
b = Node(2)
c = Node(3)
a.nextnode = b
b.nextnode = c
c.nextnode = a

print(cycle_check(c))