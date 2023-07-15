#linked list from scratch
class Node:
    def __int__(self,value):
        self.data = value
        self.node = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    #inserting into head
    def inserthead(self, value):
        node = Node(value)
        self.head = node.data
        self.node = node
