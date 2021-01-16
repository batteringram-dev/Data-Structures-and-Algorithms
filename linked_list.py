class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head
        llstr = ""
        
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
            
        print(llstr)
        
ll = LinkedList()
ll.insert_at_beginning("Mango")
ll.insert_at_beginning("Orange")
ll.insert_at_beginning("Apple")
ll.print()
    
