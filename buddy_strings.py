class Solution:
    def buddyStrings(self, A, B):
    # Fill this in.
        dist = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                if A[i:] == B[i+1:]:
                    A = A[:i] + B[i:]
                    dist += 1
                else:
                    A = A[:i] + B[i] + A[i+1:]
                    dist += 1
        if dist == 2:
            return True
        else:
            return False

print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False
