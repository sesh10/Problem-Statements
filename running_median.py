def running_median(stream):
    # Fill this in.
    pot = []
    ans = []
    for i in range(len(stream)):
        pot.append(stream[i])
        pot.sort()
        if len(pot)%2 == 0:
            med = (pot[int(len(pot)/2)-1] + pot[int(len(pot)/2)]) / 2
            ans.append(med)
        elif len(pot)%2 != 0:
            med = pot[int(len(pot)/2)]
            ans.append(med)
    print(ans)

running_median([2, 1, 4, 7, 2, 0, 5])
# 2 1.5 2 3.0 2 2.0 2
