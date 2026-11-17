"""
Why do we need functions?
- To avoid duplication of code. 
- To organize the code into blocks. 
- To help maintaining the code easily.

syntax: 
arguments-> are used to pass data to the function 
def functionName(arguments): 
    # logic 
    return value # return 
"""
import random 
def toss():
    number = random.randint(0,1)
    if number == 0:
        return "Heads"
    else:
        return "Tails"
    
side = toss() 
print(side)