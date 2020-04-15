class Solution:
    def sortColors(self, nums):
        # Fill this in.
        cmin = 0
        cmax = len(nums)-1
        x = max(nums)
        y = min(nums)
        for i in range(len(nums)):
            if nums[i] == x:
                nums.remove(x)
                nums.insert(cmax, x)
            elif nums[i] == y:
                nums.pop(i)
                nums.insert(cmin, y)    
            else:
                continue
        

nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
