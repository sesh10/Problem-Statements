# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution:
    def moveZeros(self, nums):
    # Fill this in.
        c = 0
        for i,j in enumerate(nums):
            if j == 0:
                c += 1
                nums.remove(nums[i])
        for i in range(c):
            nums.append(0)
            

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
