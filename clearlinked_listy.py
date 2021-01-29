class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        current_node = self.head
        
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        
    def prepend(self, data):
        node = Node(data)
        
        node.next = self.head
        self.head = node
# ----------------------------------------------------->        
    def insert_inbetween_node(self, prev_node, data):
        if not prev_node:
            print("Previous Node is Empty")
            return
        
        node = Node(data)
        
        node.next = prev_node.next
        prev_node.next = node
        
ll = LinkedList()
ll.append("D")
ll.append("C")
ll.append("B")
ll.append("A")
ll.insert_inbetween_node(ll.head.next, "E")
ll.print()
