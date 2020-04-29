def find_fixed_point(nums):
    # Fill this in.
    for i in range(len(nums)):
        if nums[i] == i:
            return nums[i]
    return "Not Found"

print(find_fixed_point([-5, 1, 3, 4]))
# 1
