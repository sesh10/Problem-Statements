# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

# Example 1:
# Input: [3, 3, 2, 1, 3, 2, 1]
# Output: [1, 1, 2, 2, 3, 3, 3]

def sortNums(nums):
	id1 = 0
	id2 = len(nums)-1
	i = 0
	while i <= id2:
		if nums[i] == 1:
			nums[i], nums[id1] = nums[id1], nums[i]
			i += 1
			id1 += 1
		elif nums[i] == 2:
		  	i += 1
		elif nums[i] == 3:
			nums[i], nums[id2] = nums[id2], nums[i]
			id2 -= 1
		print(nums)
	return nums


print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
