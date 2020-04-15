# You are given two linked-lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None
    self.prev = None

class Solution:
    
    def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.
        total = ListNode(0)
        while (l1 is not None or l2 is not None):
            total.val = c + l1.val + l2.val
            if (total.val>9):
                c = 1
                total.val = total.val % 10
            else:
                c = 0   
            if (l1.next is not None or l2.next is not None or total is not None):
                total.next = ListNode(0)        
                total.next.prev = total
                total = total.next
                total.val += c
            l1 = l1.next
            l2 = l2.next   
        while (total.prev is not None):
            total = total.prev
        return total

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print (result.val,)
  result = result.next
# 7 0 8
