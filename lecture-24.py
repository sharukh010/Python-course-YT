# control statements 
skip = int(input("Enter the skipping point(1-10): "))

# for i in range(1,10):
#     print(i)
#     if i == stop:
#         break 
        
for i in range(1,11):
    if i == skip:
        continue
    print(i)