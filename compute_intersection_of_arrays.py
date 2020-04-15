class Solution:
    def intersection(self, nums1, nums2):
        # Fill this in.
        ans = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                ans.append(nums1[i])
        return ans

print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))
# [9, 4]
