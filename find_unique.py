# Given a list of numbers, where every number shows up twice except for one number, find that one number.

# Example:
# Input: [4, 3, 2, 4, 1, 3, 2]
# Output: 1

def singleNumber(nums):
    # Fill this in.
    ans = []
    for i in range(len(nums)):
        if nums[i] not in ans:
            ans.append(nums[i])
        elif nums[i] in ans:
            ans.remove(nums[i])
    return ans

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1
