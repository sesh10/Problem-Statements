# Given a string with the initial condition of dominoes, where:

# . represents that the domino is standing still
# L represents that the domino is falling to the left side
# R represents that the domino is falling to the right side

# Figure out the final position of the dominoes. 
# If there are dominoes that get pushed on both ends, the force cancels out and that domino remains upright.

class Solution(object):
    def pushDominoes(self, dominoes):
        # Fill this in.
        ans = ""
        force = [0]*len(dominoes)
        f = 0
        for i in range(len(dominoes)):
            if dominoes[i] == 'R':
                f = len(dominoes)
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f-1, 0)
            force[i] += f

        f = 0
        for i in reversed(range(len(dominoes))):
            if dominoes[i] == 'L':
                f = len(dominoes)
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = max(f-1, 0)
            force[i] -= f

        for f in force:
            if f == 0:
                ans += '.'
            elif f > 0:
                ans += 'R'
            else:
                ans += 'L'
        
        return ans
        

print(Solution().pushDominoes('..R...L..R.'))
# ..RR.LL..RR
