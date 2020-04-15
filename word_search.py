# You are given a 2D array of characters, and a target string. 
# Return whether or not the word target word exists in the matrix. 
# Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.

# Example:

# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]

# Given this matrix, and the target word FOAM, you should return true, as it can be found going up-to-down in the first column.

def word_search(matrix, word):
    # Fill this in.
    tar = list(word)
    seta = []
    for s in matrix:
        if s == tar:
            return True
    for i in range(len(word)):
        for s in matrix:
            seta.append(s[i])
        if seta == tar:
            return True
        else:
            seta.clear()
    return False
            
        
        
  
matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'O', 'P'],
  ['A', 'N', 'A', 'B'],
  ['M', 'O', 'T', 'T']]
print(word_search(matrix, 'FOAM'))
# True
