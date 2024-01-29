from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=nums
        result[0]=nums[0]
        for i in range(1,len(nums)):
            result[i]=result[i-1]+nums[i]
        return result

    #     time complexity of this code is O(n)
    #     space complexity of this code is O(1)


#Over-right Approch
    def runningSum0(self, nums: List[int]) -> List[int]:
        nums[0]=nums[0]
        for i in range(1,len(nums)):
            nums[i]=nums[i-1]+nums[i]
        return nums
    #     time complexity of this code is O(n)
    #     space complexity of this code is O(1)

a=Solution()
print(a.runningSum0([1,2,3,4]))