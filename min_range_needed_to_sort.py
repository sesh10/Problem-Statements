def findRange(nums):
    # Fill this in.
    arr = []
    ans = []
    arr = sorted(nums)
    for i in range(len(nums)):
        if arr[i] != nums[i]:
            ans.append(i)
    return [min(ans),max(ans)]

print(findRange([1, 7, 9, 5, 7, 8, 10]))
# (1, 5)
