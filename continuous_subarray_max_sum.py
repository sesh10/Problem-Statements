##You are given an array of integers.
##Find the maximum sum of all possible contiguous subarrays of the array.
##
##Example:
##[34, -50, 42, 14, -5, 86]

##Given this input array, the output should be 137.
##The contiguous subarray with the largest sum is [42, 14, -5, 86].
##
##Your solution should run in linear time.


def max_subarray_sum(arr):
    # Fill this in.
    max_so_far = arr[0] 
    curr_max = arr[0] 
      
    for i in range(1,len(arr)): 
        curr_max = max(arr[i], curr_max + arr[i]) 
        max_so_far = max(max_so_far,curr_max)
    return max_so_far        
        
        

print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137
