class Node:
    def __init__(self, init_val):
        self.val = init_val
        self.next = None
    def get_val(self):
        return self.val
    def get_next(self):
        return self.next
    def set_val(self, value):
        self.val = value
    def set_next(self, next):
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def add(self, item):
        tmp = Node(item)
        tmp.set_next(self.head)
        self.head = tmp

link = SinglyLinkedList()
print(link.is_empty())
link.add(3)
print(link.is_empty())
