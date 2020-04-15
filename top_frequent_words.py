class Solution(object):
    def topKFrequent(self, words, k):
        # Fill this in.
        count = {}
        ans = []
        for i in range(len(words)):
            if words[i] not in count:
                count[words[i]] = 1
            else:
                count[words[i]] += 1
            if count[words[i]] >= k and words[i] not in ans:
                ans.append(words[i])
        return ans

words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']
