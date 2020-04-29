import math

def is_palindrome(n):
    # Fill this in.
    ans = []
    a = math.ceil(math.log10(n))
    for i in range(a):
        ans.append(n%10)
        n //= 10
    for i in range(int(a/2)+1):
        if ans[i] == ans[a-i-1]:
            c = 1
        else:
            c = 0
            return False
    return True
    

print(is_palindrome(1234321))
# True
print(is_palindrome(1234322))
# False
