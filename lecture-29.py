# Drawing Hollow Rectangle 
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of cols: "))

for row in range(1,rows+1):
    for col in range(1,cols+1):
        if row == 1 or row == rows or col == 1 or col == cols:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()