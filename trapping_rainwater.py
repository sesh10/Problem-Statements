def capacity(arr):
    # Fill this in.
    c = 0
    l = min(arr)
    d = max(arr)
##    while l != d:
##        for i in range(1,len(arr)-1):
##            if arr[i] == l:
##                if (arr[i-1]>l and arr[i+1]>l):
##                    c += min(arr[i-1]-arr[i],arr[i+1]-arr[i])
##                    arr[i] += min(arr[i-1]-arr[i],arr[i+1]-arr[i])
##        l = min(arr)
    return c
        
        
            

print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6
