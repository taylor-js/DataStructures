# Last in first out (LIFO)
queue = [] 

queue.append('John') 
queue.append('Brian') 
queue.append('Freddie') 
queue.append('Emma')
queue.append('Alison') 
queue.append('Jessica') 

print("Initial queue") 
print(queue) 

print("\nElements dequeued from queue") 
print(queue.pop(0)) 
print(queue.pop(0)) 
print(queue.pop(0)) 
print(queue.pop(0)) 
print(queue.pop(0)) 
print(queue.pop(0)) 

print("\nQueue after removing elements") 
print(queue) 

