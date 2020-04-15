class Solution(object):
    def compress(self, chars):
        # Fill this in.
        ans = []
        c = 1
        for i in range(len(chars)-1):
            if chars[i] == chars[i+1]:
                c += 1
            else:
                ans.append(chars[i])
                if c > 1:
                    ans.append(str(c))
                    c = 1
        ans.append(chars[i])
        ans.append(str(c))
        return ans
        
            

print(Solution().compress(['a', 'a', 'b', 'c', 'c', 'c']))
# ['a', '2', 'b', 'c', '3']
