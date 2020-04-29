def first_recurring_char(s):
    # Fill this in.
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return s[i]
    return None
  
print(first_recurring_char('qwertty'))
# t

print(first_recurring_char('qwerty'))
# None
