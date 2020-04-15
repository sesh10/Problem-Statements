def first_missing_positive(nums):
    # Fill this in.
    for i in range(1,max(nums)):
        if i in nums:
            continue
        else:
            return i
    return False

print(first_missing_positive([3, 4, -1, 1]))
# 2
