a = int(input("Enter the number: "))
ans1 = []
ans2 = []
ans1.append(a)
print("Initially: ",str(ans1)) 
k = int(input("After how many turns: "))

def looksay(arr1, arr2):
    c = 1
    i = 0
    while True:
        if i == len(arr1)-1:
            arr2.append(c)
            arr2.append(arr1[i])
            c = 1
            break
        elif (arr1[i] == arr1[i+1] and i < len(arr1)-1):
            c += 1
        else:
            arr2.append(c)
            arr2.append(arr1[i])
            c = 1
        i += 1
    arr1.clear()

for i in range(k):
    if (i%2 == 0):
        looksay(ans1, ans2)
        print("".join(map(str, ans2)))
    else:
        looksay(ans2, ans1)
        print("".join(map(str, ans1)))
