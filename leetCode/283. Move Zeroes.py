from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # nums_count=nums.count(0)
        # nums = [i for i in nums if i != 0]
        # for i in range (nums_count):
        #     nums.append(0)
        # return nums
        nums_count=nums.count(0)
        nums[:] = [i for i in nums if i != 0]
        nums.extend([0] * nums_count)
        print(nums)
a=Solution
print(a.moveZeroes(None,[0,1,0,3,12]))