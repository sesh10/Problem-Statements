def getBonuses(performance):
    # Fill this in.
    ans = []
    for i in range(len(performance)):
        c = 1
        if i == 0:
            if performance[0] > performance[1]:
                ans.append(c+1)
            else:
                ans.append(c)
            continue
        if i == len(performance)-1:
            if performance[i] > performance[i-1]:
                ans.append(c+1)
            else:
                ans.append(c)
            break
        if (performance[i]>performance[i-1] and performance[i]>performance[i+1]):
            ans.append(c + 2)
        elif performance[i]<performance[i-1] and performance[i]<performance[i+1]:
            ans.append(c)
        else:
            ans.append(c+1)
        
    return ans
            
        

print(getBonuses([1, 2, 3, 2, 3, 5, 1]))
# [1, 2, 3, 1, 2, 3, 1]
