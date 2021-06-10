class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty! ")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end="")
                n = n.nref

    def print_LL_reverse(self):
        if self.head is None:
            print("Linked List is empty! ")
        else:
            n = self.head
            while n is not None:
                n = n.nref
            while n is not None:
                print(n.data, "-->", end="")
                n = n.pref

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is empty! ")

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_after(self, data, x):
        if self.head is None:
            print("Linked List is empty! ")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given node is not present! ")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node               # Confusing part. Inserting new node before the last node
                n.nref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Linked list is empty! ")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given node is not present! ")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node                # Confusing part. Inserting new node after the first node
                n.pref = new_node

    def delete_begin(self):
        if self.head is None:
            print("DLL is empty! ")
            return
        if self.head.nref is None:
            self.head = None
            print("DLL is empty after deleting the node! ")
        else:
            self.head = self.head.nref
            self.head.pref = None

    def delete_end(self):
        if self.head is None:
            print("DLL is empty! ")
            return
        if self.head.nref is None:
            self.head = None
            print("DLL is empty after deleting the node! ")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    def delete_by_value(self, x):
        if self.head is None:
            print("DLL is empty! ")
            return
        if self.head.nref is None:
            if x == self.head.data:
                self.head = None
            else:
                print("X not present in DLL. ")
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print("X not present in DLL! ")


dll1 = DoublyLL()
dll1.add_begin(10)
dll1.add_begin(20)
dll1.delete_by_value(20)
dll1.print_LL()
dll1.print_LL_reverse()
