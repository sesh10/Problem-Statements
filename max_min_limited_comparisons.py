def find_min_max(nums):
    # Fill this in.
    a = 99999
    b = 0
    for i in range(len(nums)):
        if nums[i] > b:
            b = nums[i]
        if nums[i] < a:
            a = nums[i]
    return (a,b)

print(find_min_max([3, 5, 1, 2, 4, 8]))
# (1, 8)
