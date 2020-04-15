def findRanges(nums):
    # Fill this in.
    ans = []
    a = nums[0]
    for i in range(1,len(nums)):
        if (nums[i]==nums[i-1] or nums[i]==nums[i-1]+1):
            if i == len(nums)-1:
                ans.append(str(a)+'->'+str(nums[i]))
            continue
        else:
            ans.append(str(a)+'->'+str(nums[i-1]))
            a = nums[i]
            if i == len(nums)-1:
                ans.append(str(a)+'->'+str(nums[i]))
    return ans
    

print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']
