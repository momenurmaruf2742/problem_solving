from typing import List

# it took more time


# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         # b= list(nums)
#         # n= len(b)
#         re=[]
#         for i in range(1,len(nums)+1):
#             if i not in nums:
#                 re.append(i)
#         return re


# a=Solution
# print(a.findDisappearedNumbers(None,[4,3,2,7,8,2,3,1]))
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
    
        # Step 2: Identify the missing numbers (numbers that are still positive)
        disappeared_numbers = []
        for i, num in enumerate(nums, 1):
            if num > 0:
                disappeared_numbers.append(i)
        
        return disappeared_numbers

# Example usage:
nums = [4, 3, 2, 7, 8, 2, 1, 3]
a=Solution
print(a.findDisappearedNumbers(None,nums))