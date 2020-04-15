# Given a list, find the k-th largest element in the list.
# Input: list = [3, 5, 2, 4, 6, 8], k = 3
# Output: 5


def findKthLargest(nums, k):
    # Fill this in.
    for i in range(k-1):
        nums.remove(max(nums))
    return max(nums)

print(findKthLargest([3, 5, 2, 4, 6, 8], 3))
# 5
