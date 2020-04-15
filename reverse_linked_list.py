# Given a singly-linked list, reverse the list. 
# This can be done iteratively or recursively. Can you get both solutions?

# Example:
# Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
# Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
  
  # Function to print the list
    def printList(self):
        node = self
        output = '' 
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

  # Iterative Solution
    def reverseIteratively(self, head):
    # Implement this.
        prev = None
        bun = head
        while bun != None:
            next = bun.next
            bun.next = prev
            prev = bun
            bun = next
        head = prev
        

  # Recursive Solution      
    def reverseRecursively(self, node):
    # Implement this.
        if node is None:
            return 
        elif node.next is None: 
            self.head = node 
            return
        else:
            self.reverseRecursively(node.next) 
            node.next.next = node 
            node.next = None


# Test Program
# Initialize the test list: 
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
#testHead.reverseIteratively(testHead)
testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4
