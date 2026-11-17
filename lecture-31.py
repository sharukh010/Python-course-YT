# type hints and doc strings 

def add(num1: float | int,num2: float | int)-> float | int:
    """
    It takes two numbers add them and return result.

    Arg: 
    num1 (float | int) - this is first number. 
    num2 (float | int) - this is second number.

    Return:
    result (float | int) - this is the sum of num1 and num2.
    """
    result = num1 + num2 
    return result 

result = add(1,2)
print(result)
