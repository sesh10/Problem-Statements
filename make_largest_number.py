def largestNum(nums):
    # Fill this in.
    ans = []
    for i in range(len(nums)):
        n = ''
        n += str(nums[i])
        for j in range(len(sorted(nums[:i:]))):
            n += str(nums[j])
        ans.append(int(n))
    print(ans)
    return max(ans)
            

print(largestNum([17, 7, 2, 45, 72]))
# 77245217
