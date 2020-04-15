# There are n people lined up, and each have a height represented as an integer. 
# A murder has happened right in front of them, and only people who are taller than everyone in front of them are able to see what has happened. 
# How many witnesses are there?

def witnesses(h):
    # Fill this in.
    witn = []
    for i in reversed(range(len(h))):
        if not witn:
            witn.append(h[i])
        elif (all(h[i] > a for a in h[i+1:])):
            witn.append(h[i])                
    return len(witn)
        
        

print(witnesses([3, 6, 3, 4, 1]))
# 3
