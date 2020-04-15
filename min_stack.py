class minStack(object):
    def __init__(self):
        # Fill this in.
        self.arr = []

    def push(self, x):
        # Fill this in.
        self.arr.append(x)

    def pop(self):
        # Fill this in.
        self.arr.pop()

    def top(self):
        # Fill this in.
        return self.arr[-1]

    def getMin(self):
        # Fill this in.
        return min(self.arr)

x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
# -3
x.pop()
print(x.top())
# 0
print(x.getMin())
# -2
