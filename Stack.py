# First in First out (FIFO)
stack = [] 

stack.append('John') 
stack.append('Brian') 
stack.append('Freddie') 
stack.append('Emma')
stack.append('Alison') 
stack.append('Jessica') 

print('Initial stack') 
print(stack) 

print('\nElements poped from stack:') 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 

print('\nStack after elements are poped:') 
print(stack)