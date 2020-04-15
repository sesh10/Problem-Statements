# Given a list of numbers, find if there exists a pythagorean triplet in that list. 
# A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2

# Example:
# Input: [3, 5, 12, 5, 13]
# Output: True
# Here, 5^2 + 12^2 = 13^2.

def findPythagoreanTriplets(nums):
    # Fill this in.
    list = []
    list = [x ** 2 for x in nums]
    for a in list:
        for b in list:
            c = a + b
            if c in list:
                return True
    return False

print(findPythagoreanTriplets([3, 12, 5, 13]))
# True
