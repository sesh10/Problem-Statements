def isSorted(words, order):
    # Fill this in.
    for i in range(1, len(words)):
        for j in range(len(words[i-1])):
            if order.index(words[i][j]) < order.index(words[i-1][j]):
                return False
            else:
                continue
    return True

print(isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False
print(isSorted(["zyx", "zyxw", "zyxwy"], "zyxwvutsrqponmlkjihgfedcba"))
# True
