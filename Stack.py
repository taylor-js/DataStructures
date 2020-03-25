# First in First out (FIFO)

class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def push(self,val):
        return self.stack.append(val)

    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

stack = Stack()

stack.push('John') 
stack.push('Brian') 
stack.push('Freddie') 
stack.push('Emma')
stack.push('Alison') 
stack.push('Jessica') 

print('\nElements poped from stack:') 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 