class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer

def merge(lists):
    # Fill this in.
    ans = Node(0)
    row1 = lists[0]
    row2 = lists[1]
    head = ans
    while row1 or row2 is not None:
        if row1 is None:
            ans.next = row2 
            ans = ans.next
            row2 = row2.next
            continue
        if row2 is None:
            ans.next = row1
            ans = ans.next
            row1 = row1.next
            continue
        if (row1.val < row2.val):
            ans.next = row1
            ans = ans.next
            row1 = row1.next
        else:            
            ans.next = row2
            ans = ans.next
            row2 = row2.next    
    return head
        
    

a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print(merge([a, b]))
# 123456
