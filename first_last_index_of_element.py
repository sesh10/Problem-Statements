# Given a sorted array, A, with possibly duplicated elements, 
# find the indices of the first and last occurrences of a target element, x. 
# Return -1 if the target is not found.

# Example:
# Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
# Output: [6,8]

# Input: A = [100, 150, 150, 153], target = 150
# Output: [1,2]

# Input: A = [1,2,3,4,5,6,10], target = 9
# Output: [-1, -1]

class Solution: 
    def getRange(self, arr, target):
    # Fill this in.
        bound = []
        for i in range(len(arr)-1):
            if target is arr[i]:
                if not bound:
                    bound.append(i)
                if (target<arr[i+1]):
                    if i not in bound:
                        bound.append(i)
            if (target is arr[i+1] and arr[i+1] is arr[-1]):
                bound.append(i+1)
            
        return bound
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]
