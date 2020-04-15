# You 2 integers n and m representing an n by m grid, 
# determine the number of ways you can get from the top-left to the bottom-right of the matrix y going only right or down.

# Example:
# n = 2, m = 2

# This should return 2, since the only possible routes are:
# Right, down
# Down, right.

def num_ways(n, m):
    # Fill this in.
    if n == 1:
        return 1
    if m == 1:
        return 1
    return num_ways(n-1,m) + num_ways(n,m-1)

print(num_ways(3, 3))
# 2
