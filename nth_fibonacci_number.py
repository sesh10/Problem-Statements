class Solution():
    def fibonacci(self, n):
        # fill this in.
        ans = [0, 1]
        for i in range(2, n+1):
            c = ans[i-1] + ans[i-2]
            ans.append(c)
        return ans.pop()

n = 9
print(Solution().fibonacci(n))
# 34
