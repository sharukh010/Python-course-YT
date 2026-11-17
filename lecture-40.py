# list slicing 
# nums = [1,2,3,4,5]
# # print(nums[:3])# by default it will start with 0 
# # print(nums[0:])# by default it will start with 0 
# # print(nums[0:4:2])# we can write a thrid parameter for step 
# # print(nums[::-1])
# print(nums[-5:-2])
# list comprehension 
# nums = [1,1,1,1,1]
# nums = [] 
# for i in range(5):
#     nums.append(1)
# nums = [1 for i in range(5)]
# nums = [i+1 for i in range(5)]
# print(nums)
# rows = 4
# cols = 4
# board = [[" " for i in range(cols)] for j in range(rows)]
# print(board)
nums = [10,20,30,40,50]
result = [(num/10) for num in nums]
print(result)