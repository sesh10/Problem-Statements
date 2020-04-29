KAPREKAR_CONSTANT = 6174

def num_kaprekar_iterations(n):
    # Fill this in.
    c = 0
    alert = 0
    while(alert!=1):
        a = str(n)
        desc = [int(a[i]) for i in range(len(a))]
        asc = [int(a[i]) for i in range(len(a))]
        desc.sort(reverse=True)
        asc.sort()
        if len(desc) != 4:
            desc.append(0)
        desc_num = int(''.join(str(x) for x in desc))
        asc_num = int(''.join(str(y) for y in asc))
        result = desc_num - asc_num
        c += 1
        if result == KAPREKAR_CONSTANT:
            alert = 1
        else:
            n = result
    return c
        

print(num_kaprekar_iterations(123))
# 3
# Explanation:
#  3210 - 123 = 3087
#  8730 - 0378 = 8352
#  8532 - 2358 = 6174 (3 iterations)
