
import operator
import math

def problem():
    tokens = ["4","13","5","/","+"]

    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.floordiv
    }
    
    stack = []
    t = len(tokens)

    for i in range(t):
        print(stack)
        if tokens[i].lstrip('-').isdigit():
            num = int(tokens[i])
            if num < 0:
                stack.append(math.ceil(num))
            else:
                stack.append(num)
        else:
            res = ops[tokens[i]](stack[-2], stack[-1])
            stack.pop()
            stack.pop()
            stack.append(res)
            
            
     
    return int(stack[-1])
            


print(problem())
print(math.trunc(6/-132))
