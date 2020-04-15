def calcAngle(h, m):
    # Fill this in.
    d = ((h * 5) + (m / 12)) % 60
    if (m-d) > 30:
        ans = (60 - m + d) * 6
    else:
        ans = (m - d) * 6
    return ans
    

print(calcAngle(3, 30))
# 75
print(calcAngle(12, 30))
# 165
