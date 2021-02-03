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

    def len_iterative(self):
        count = 0
        current_node = self.head
        
        while current_node:
            count += 1
            current_node = current_node.next
            return count
            
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)
# -------------------------------------------------->

    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return 

        prev_1 = None 
        curr_1 = self.head 
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1 
            curr_1 = curr_1.next

        prev_2 = None 
        curr_2 = self.head 
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2 
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return 

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next  
            
            
ll = LinkedList()
ll.append("D")
ll.append("C")
ll.append("B")
ll.append("A")

ll.swap_nodes("B", "C")
ll.print()
