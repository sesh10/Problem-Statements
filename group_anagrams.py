import collections

def groupAnagramWords(strs):
    # Fill this in.
    ans = []
    groups = collections.defaultdict(list)
    for word in strs: 
        groups["".join(sorted(word))].append(word) 
  
    # Print all anagrams together 
    for group in groups.values(): 
        ans.append(list(group))
    return ans
        

print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]
