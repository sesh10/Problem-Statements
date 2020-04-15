# You are given a positive integer N which represents the number of steps in a staircase. 
# You can either climb 1 or 2 steps at a time. 
# Write a function that returns the number of unique ways to climb the stairs.

def staircase(N):
    # Fill this in.
    print(N)
    if N == 1:
        return 1
  
    if N == 2:
        return 2
    
    return staircase(N - 1) + staircase(N - 2)
        
    
  
print(staircase(4))
# 5
#print(staircase(5))
# 8
