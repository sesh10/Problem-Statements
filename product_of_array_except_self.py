def products(nums):
    # Fill this in.
    ans = []
    for i in range(len(nums)):
        c = 1
        for j in range(len(nums)):
            if j != i:
                c *= nums[j]
        ans.append(c)
    return ans
    

print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]
