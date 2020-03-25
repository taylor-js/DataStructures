# Last in first out (LIFO)

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,val):
        self.queue.insert(0,val)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

queue = Queue()

queue.enqueue('John') 
queue.enqueue('Brian') 
queue.enqueue('Freddie') 
queue.enqueue('Emma')
queue.enqueue('Alison') 
queue.enqueue('Jessica') 

print("\nElements dequeued from queue") 
print(queue.dequeue()) 
print(queue.dequeue()) 
print(queue.dequeue()) 
print(queue.dequeue()) 
print(queue.dequeue()) 
print(queue.dequeue()) 