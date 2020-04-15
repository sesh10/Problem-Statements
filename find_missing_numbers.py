class Solution(object):
    def findDisappearedNumbers(self, nums):
        # Fill this in.
        ans = []
        for i in range(1, len(nums)):
            if i not in nums:
                ans.append(i)
        return ans

nums = [4, 6, 2, 6, 7, 2, 1]
print(Solution().findDisappearedNumbers(nums))
# [3, 5]
