class DoublyLinkedList():
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None
a = DoublyLinkedList(1)
b = DoublyLinkedList(2)
c = DoublyLinkedList(3)
a.next_node = b
b.prev_node = a
b.next_node = c
c.prev_node = b

#For Circular Linked List
c.next_node = a
a.prev_node = c
