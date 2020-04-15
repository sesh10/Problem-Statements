# You are given an array of integers in an arbitrary order. 
# Return whether or not it is possible to make the array non-decreasing by modifying at most 1 element to any value.

# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
# Example:
# [13, 4, 7] should return true, since we can modify 13 to any value 4 or less, to make it non-decreasing.

# [13, 4, 1] however, should return false, since there is no way to modify just one element to make the array non-decreasing.


def check(list):
    # Fill this in.
    c = 0
    for i in range(len(list)-1):
        if (list[i] <= list[i+1]):
            continue
        else:
            list[i] = list[i+1]
            c += 1
    if (c==1):
        return True
    else:
        return False
    

print(check([13, 4, 7]))
# True
print(check([5,1,4,2,5]))
# False
