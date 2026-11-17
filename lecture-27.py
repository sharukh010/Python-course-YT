# Drawing Triangle Pattern 
rows = int(input("Enter the number of rows: "))
# cols = 1 
# for row in range(1,rows+1): # rows 
#     for col in range(1,cols+1): # cols 
#         print("*",end=" ")
#     print() # this moves to next line 
#     cols += 1 # cols = cols + 1 
for row in range(1,rows+1): # rows 
    for col in range(1,row+1): # cols 
        print("*",end=" ")
    print() # this moves to next line 
   
    