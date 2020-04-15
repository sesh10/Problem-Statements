class Solution():
    def plusOne(self, digits):
        # Fill this in.
        c = 0
        digits[-1] = (digits[-1] + 1)
        if ((digits[-1]) >= 10):
            digits[-1] = (digits[-1]) % 10
            c = 1
        else:
            return digits
        i = 1
        while i <= len(digits):
            if  (digits[-(1+i)] + c) >= 10:
                digits[-(1+i)] = (digits[-(1+i)] + 1) % 10
                c = 1
            else:
                digits[-(1+i)] = (digits[-(1+i)] + c)
                c = 0
                return digits
            i += 1
        return digits      
            
num = [2, 9, 9]
print(Solution().plusOne(num))
# [3, 0, 0]
