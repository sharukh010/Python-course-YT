# optional parameters and variable parameters
"""
optional parameters: You can provide default values to the arguments and skip them while calling the function. This doesn't give any error.

variable parameters: Your function can have variable parameters (0,1,2,3,4)

""" 

# def add(num1 = 0,num2 = 0):
#     return num1 + num2 
def add(*numbers):
    result = 0 
    for num in numbers:
        result += num 
    return result 

print(add(1))
print(add(1,2))
print(add(1,2,3,4))
# print("hello, world",123,4,56)