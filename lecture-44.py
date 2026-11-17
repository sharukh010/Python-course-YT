# Deep Copy and shallow copy 
import copy 
# nums = [1,2,3,4]
# # print(id(nums))
# nums_2d = [nums]
# nums[2] = 5 
# # print(id(nums_2d[0]))
# print(nums_2d)
nums = [[1,2],[3,4],[5,6],10]
# nums_copy = nums.copy()
# nums[0][0] = 9 
# nums[3] = 12
# print(nums_copy)
nums_copy = copy.deepcopy(nums)
nums[0][0] = 9 
print(nums_copy)
print(nums)