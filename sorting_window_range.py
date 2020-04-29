def min_window_to_sort(nums):
    # Fill this in.
    alert = 0
    l = len(nums) - 1
    c = 0
    while(alert!=1):
        if (nums[0] == min(nums) and nums[-1] == max(nums)):
            nums.pop(0)
            nums.pop(-1)
            c += 1
            l -= 1
        elif nums[0] != min(nums):
            if nums[-1] == max(nums):
                nums.pop(-1)
                l -= 1
            else:
                alert = 1
        elif nums[-1] != max(nums):
            if nums[0] == min(nums):
                nums.pop(0)
                c += 1
            else:
                alert = 1
    return (c, l)
            
                
        
  
print(min_window_to_sort([2, 4, 7, 5, 6, 8, 9]))
# (2, 4)
