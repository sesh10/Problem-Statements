# Implement a class for a stack that supports all the regular functions (push, pop) 
# and an additional function of max() which returns the maximum element in the stack 
# (return None if the stack is empty). Each method should run in constant time.

class MaxStack:
    def __init__(self):
    # Fill this in.
        self.stack = []

    def push(self, val):
    # Fill this in.
        self.stack.append(val)

    def pop(self):
    # Fill this in.
        self.stack.pop()

    def max(self):
    # Fill this in.
        return max(self.stack)
        

s = MaxStack()
s.push(1)
s.push(2)
s.push(4)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
