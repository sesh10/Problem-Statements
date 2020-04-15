def hIndex(publications):
    # Fill this in.
    for i in range(max(publications)):
        c = 0
        for j in range(len(publications)):
            if publications[j] >= i:
                c += 1
        if c == i:
            return c
    return None
            
    
print(hIndex([5, 3, 3, 1, 0]))
# 3
