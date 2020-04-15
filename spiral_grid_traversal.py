# You are given a 2D array of integers. 
# Print out the clockwise spiral traversal of the matrix.
# Example:

# grid = [[1,  2,  3,  4,  5],
#         [6,  7,  8,  9,  10],
#         [11, 12, 13, 14, 15],
#         [16, 17, 18, 19, 20]]

# The clockwise spiral traversal of this array is:
# 1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12


def matrix_spiral_print(M):
    # Fill this in.
    ans = []
    for i in range(len(M)):
        a = i
        if a < len(M)/2:
            for j in range(i,len(M[i])):
                ans.append(M[i][j])
                if j == len(M[i])-i-1:
                    while i != len(M)-a-1:
                        ans.append(M[i+1][j])
                        i += 1
                if i == len(M)-a-1:
                    while j > a:
                        ans.append(M[i][j-1])
                        j -= 1
                    while i-1 > a:
                        ans.append(M[i-1][j])
                        i -= 1
                    if i-1 > a and j<a:
                        continue
                    elif j >= a:
                        break
    print(" ".join(str(a) for a in ans))        
    

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
