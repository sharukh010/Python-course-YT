# Calculator Application 
print("Simple Calculator")
print("Supported Opertors : + , - , x , / , ^")
print("Format: Seperate the numbers and operators using a space")
print("Ex: 23 + 24")
n1,op,n2 = input("Expression: ").split(" ")
n1 = int(n1)
n2 = int(n2)
# [+,-,x,/,^]
match op:
    case "+":
        result = n1 + n2 
    case "-":
        result = n1 - n2 
    case "x":
        result = n1 * n2 
    case "/":
        if n2 == 0:
            print("Cannot divide with Zero")
            result = "NA"
        else:
            result = n1 / n2 
    case "^":
        result = n1 ** n2 
    case _ :
        result = None 
# 23 x 4 = result 
if result != None:  
    print(f"{n1} {op} {n2} = {result}")
else:
    print("Invalid operator, Try again with supported operators")