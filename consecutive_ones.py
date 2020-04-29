def longest_run(n):
    # Fill this in.
    a = bin(n)
    count = []
    c = 0

    text = str(a)
    print(text)
    for i in range(2, len(text)):
        if text[i] == '1':
            c += 1
            if i == len(text)-1:
                count.append(c)
        else:
            count.append(c)
            c = 0
    return max(count)

print(longest_run(65535))
# 4
