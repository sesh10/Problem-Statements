# Given a string, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s):
        c = 1
        ans = []
        for i in range(len(s)-1):
            if ord(s[i]) == ord(s[i+1])-1:
                c += 1
            else:
                ans.append(c)
                c = 1
        return max(ans)

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
