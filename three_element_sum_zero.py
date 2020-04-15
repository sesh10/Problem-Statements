class Solution(object):
    def threeSum(self, nums):
        # Fill this in.
        ans = []
        tri = []
        for i in range(len(nums)-2):
            c = 0
            for j in range(i,i+3):
                c += nums[j]
                tri.append(nums[j])
            if c == 0:
                if tri not in ans:
                    ans.append(list(tri))
            tri.clear()
        return ans
                

# Test Program
nums = [1, -2, 1, 0, 5]
print(Solution().threeSum(nums))
# [[-2, 1, 1]]
