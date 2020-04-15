# A palindrome is a sequence of characters that reads the same backwards and forwards. 
# Given a string, s, find the longest palindromic substring in s.

# Example:
# Input: "banana"
# Output: "anana"

# Input: "million"
# Output: "illi"

class Solution: 
    def longestPalindrome(self, s):
    # Fill this in.
        f = len(s) +1
        length = 0
        l = []
        for j in range(0,f):
            for i in range(j+1,f):
                var = s[j:i]
                if var == var[::-1] and len(var) != 1:
                    if length <= len(var):
                        length = len(var)
                        l.append(var)
        return l[-1]
        
# Test program
s = "forgeeksskeegfor"
print(str(Solution().longestPalindrome(s)))
# racecar
