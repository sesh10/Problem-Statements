# You are given an array of integers. Return the largest product that can be made by multiplying any 3 integers in the array.

# Example:
# [-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.


def maximum_product_of_three(lst):
    # Fill this in.
    c = 0
    for i in range(0,len(lst),2):
        for j in range(i+1,len(lst)):
            for k in range(j+1,len(lst)):
                ans = lst[i]*lst[j]*lst[k]
                if ans > c:
                    c = ans

    return c

print(maximum_product_of_three([-4, -4, 9, 8]))
# 128
