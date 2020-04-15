def longest_substring_with_k_distinct_characters(s, k):
    # Fill this in.
    ans = []
    for i in range(len(s)):
        c = 0
        for j in range(i,len(s)):
            if c == 0:               #first letter
                c += 1
                d = 1
            elif s[j] == s[j-1]:    # previous letter same
                c += 1
            elif s[j] != s[j-1]:
                if d == k:          # if limit of characters
                    ans.append(c)
                    break
                d += 1
                c += 1
            if (j==(len(s)-1) and d==k):
                ans.append(c)
            
    print(ans)
    return(max(ans))
        
                

print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 characters)
