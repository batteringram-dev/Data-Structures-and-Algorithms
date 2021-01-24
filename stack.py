# Stack using List.

s = []

s.append("https://www.cnn.com/")
s.append("https://www.cnn.com/world")
s.append("https://www.cnn.com/india")
s.append("https://www.cnn.com/china")

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())


# Stack using Deque.

from collections import deque
stack = deque()

stack.append("https://www.cnn.com/")
stack.append("https://www.cnn.com/world")
stack.append("https://www.cnn.com/india")
stack.append("https://www.cnn.com/china")
stack.pop()
print(stack)

# Stack using classes

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def is_empty(self):
        return self.items == 0
        
    def get_stack(self):
        return self.items
        
s = Stack()
s.push("A")
s.push("B")
s.push("C")
print(s.get_stack())
s.pop()
print(s.get_stack())
