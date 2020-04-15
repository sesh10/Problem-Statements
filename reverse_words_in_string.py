class Solution:
    def reverseWords(self, str):
        return " ".join(word[::-1] for word in str.split(" "))
        
        
print(Solution().reverseWords("The cat in the hat"))
# ehT tac ni eht tah
