def find_continuous_k(list, k):
    # Fill this in.
    ans = []
    for i in range(len(list)-1):
        c = list[i]
        for j in range(i+1,len(list)):
            c += list[j]
            if c == k:
                return list[i:j+1]
            

print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))
# [2, 5, 7]
