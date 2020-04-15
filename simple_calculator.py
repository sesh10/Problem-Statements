# Given a mathematical expression with just single digits, plus signs, negative signs, and brackets, evaluate the expression. 
# Assume the expression is properly formed.

# Example:
# Input: - ( 3 + ( 2 - 1 ) )
# Output: -4

def eval(exp):
    # Fill this in.
    num = []
    op = []
    stack = []
    for i in range(len(exp)):
        if exp[i] in '0123456789':
            num.append(int(exp[i]))
        if exp[i] == '+' or exp[i] == '-':
            op.append(exp[i])
        if exp[i] == ')':
            c2 = num.pop()
            sign = op.pop()
            c1 = num.pop()
            if sign == '+':
                num.append(c1+c2)
            elif sign == '-':
                num.append(c1-c2) 
    if op:
        fin = op.pop() + str(num.pop())
        return fin
    return num.pop()
    
            
        
    

print(eval('-( 3 + ( 2 - 1 ) )'))
# -4
