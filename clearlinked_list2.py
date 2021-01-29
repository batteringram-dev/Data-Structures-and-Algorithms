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
      
    def insert_inbetween_node(self, prev_node, data):
        if not prev_node:
            print("Previous Node is Empty")
            return
        
        node = Node(data)
        
        node.next = prev_node.next
        prev_node.next = node
# ------------------------------------------------------->     
    def delete_node(self, key):
        current_node = self.head
        
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next
            
        if current_node is None:
            return
        
        prev.next = current_node.next
        current_node = None
        
    def del_node_at_pos(self, pos):
        current_node = self.head
        
        if pos == 0:
            self.head = current_node.next
            current_node = None
            return
        
        prev = None
        count = 1
        while current_node and count != pos:
            prev = current_node
            current_node = current_node.next
            count += 1
            
        if current_node is None:
            return
        
        prev.next = current_node.next
        current_node = None
            
ll = LinkedList()
ll.append("D")
ll.append("C")
ll.append("B")
ll.append("A")
ll.del_node_at_pos(1)
ll.print()
