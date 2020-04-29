def has_character_map(str1, str2):
    # Fill this in.
    match = {}
    for i in range(len(str1)):
        if str1[i] and str2[i]:
            if str1[i] not in match.keys():
                match[str1[i]] = str2[i]
            else:
                return False
    return True
            

print(has_character_map('abc', 'def'))
# True
print(has_character_map('aac', 'def'))
# False
