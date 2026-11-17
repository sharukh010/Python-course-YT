# Drawing Rectangle pattern 
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of cols: "))

for row in range(1,rows+1):
    for col in range(1,cols+1):
        print("*",end=" ")
    print() # this is to move to next line 