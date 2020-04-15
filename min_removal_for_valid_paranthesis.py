def count_invalid_parenthesis(string):
    # Fill this in.
    ans = []
    c = 0
    for i in range(len(string)):
        if string[i] == '(':
            ans.append(string[i])
        if string[i] == ')':
            if len(ans) < 1:
                c += 1
            else:
                ans.pop()
    return c

print(count_invalid_parenthesis("()())()"))
# 1
