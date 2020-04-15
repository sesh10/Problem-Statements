# Given a linked list of integers, remove all consecutive nodes that sum up to 0.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def removeConsecutiveSumTo0(node):
    # Fill this in.
    c = []
    count = 0
    i = 0
    head = node
    h = []
    while node is not None:
        c.append(node.value)
        node = node.next
    while c:
        count += c[i]
        if count == 0:
            for a in range(i+1):
                c.pop(0)
            i = 0
            count = 0
            continue
                
        if i == len(c)-1 and (count+c[i] != None):
            h.append(c[0])
            c.pop(0)
            count = 0
            i = 0
            continue
        i += 1
        
    ans = head           
    for i in range(len(h)):
        ans.value = h[i]
        if (i+1 == len(h)):
            break
        ans = ans.next
    ans.next = None
    return head

node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)
while node:
    print(node.value,)
    node = node.next
# 10
