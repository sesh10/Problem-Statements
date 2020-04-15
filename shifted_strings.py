def is_shifted(a, b):
    # Fill this in.
    for i in range(1, len(a)):
        if b == a[-i:] + a[:-i]:
            return True
    return False
  
print(is_shifted('abcde', 'cdeab'))
# True
