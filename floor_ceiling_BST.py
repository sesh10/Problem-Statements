# Given an integer k and a binary search tree, 
# find the floor (less than or equal to) of k, and the ceiling (larger than or equal to) of k. 
# If either does not exist, then print them as None.

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
    # Fill this in.
    node = root_node
    ans = []
    while node.left or node.right:
        if (k < node.value):
            ceil = node
            node = node.left
            floor = node
        elif (k > node.value):
            ceil = node
            node = node.right
            floor = node
    ans.append(ceil.value)
    ans.append(floor.value)
    return ans
            
    

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print(findCeilingFloor(root, 11))
# (4, 6)
