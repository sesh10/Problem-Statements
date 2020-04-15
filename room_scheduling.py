def room_sched(lec):
    # Fill this in
    lec.sort()
    print(lec)
    c = 1
    i = 1
    sel = lec[0]
    while i != len(lec):
        if lec[i][0] > sel[1]:
            c += 1
            sel = lec[i]
        i += 1

    return c
            

# Number of rooms to be scheduled
print(room_sched([(30, 75), (0, 50), (60, 150)]))
# 2
