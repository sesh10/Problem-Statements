##Implement a queue class using two stacks.
##A queue is a data structure that supports the FIFO protocol (First in = first out).
##Your class should support the enqueue and dequeue methods like a standard queue.

class Queue:
    def __init__(self):
    # Fill this in.
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, val):
    # Fill this in.
        self.stack1.append(val)
        self.stack2 = self.stack1[::-1]

    def dequeue(self):
    # Fill this in.
        return self.stack2.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3
