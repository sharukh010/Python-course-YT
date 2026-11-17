# Drawing square pattern 
rows = int(input("Enter the rows values: "))

# Nested loop 
# outer loop -> 1 execution 
# inner loop -> rows executions 10 x 10 == 100 
# row = 1 outer loop 
# col  = 5 
for row in range(1,rows+1): # outer loop 
    for col in range(1,rows+1):# inner loop 
        print("*",end=" ")
    print()# this moves to next row
