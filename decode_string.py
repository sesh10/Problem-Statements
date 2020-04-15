def decodeString(s):
    # Fill this in.
    for i in range(len(s)):
        if s[i] is int:
            return True
        else:
            return False
        
        

print(decodeString('2[a2[b]c]'))
# abbcabbc
