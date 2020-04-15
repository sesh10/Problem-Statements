# Given a sequence of numbers, find the longest sequence that contains only 2 unique numbers.

# Example:
# Input: [1, 3, 5, 3, 1, 3, 1, 5]
# Output: 4
# The longest sequence that contains just 2 unique numbers is [3, 1, 3, 1]

def findSequence(seq):
    # Fill this in.
    count = []
    seta = []
    c = 0
    for i in range(len(seq)):
        print("count",i)
        if len(seta) != 2:
            seta.append(seq[i])
            c += 1
        else:
            if seq[i] in seta:
                c += 1
            else:
                seta.clear()
                count.append(c)
                c = 2
                seta.append(seq[i-1])
                seta.append(seq[i])
    return max(count)
                
            

print(findSequence([1, 3, 5, 3, 1, 3, 1, 5]))
# 4
