# Given two strings, determine the edit distance between them. 
# The edit distance is defined as the minimum number of edits (insertion, deletion, or substitution) needed to change one string to the other.

# For example, "biting" and "sitting" have an edit distance of 2 (substitute b for s, and insert a t).

def distance(s1, s2):
    # Fill this in.
    dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if s1[i:] == s2[i+1:]:
                s1 = s1[:i] + s2[i:]
                dist += 1
            else:
                s1 = s1[:i] + s2[i] + s1[i+1:]
                dist += 1    
    return dist
        
         
print(distance('biting', 'sitting'))
# 2

