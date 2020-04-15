# You are given a list of numbers, and a target number k. 
# Return whether or not there are two numbers in the list that add up to k.

# Example:
# Given [4, 7, 1 , -3, 2] and k = 5,
# return true since 4 + 1 = 5.

def two_sum(list, k):
    # Fill this in.
    for a in list[0:]:
        for b in list[1:]:
            if(a+b == k):
                return True
            elif (a+b != k):
                continue
            else:
                return False
            

print(two_sum([4,7,1,-3,0], 5))
# True
