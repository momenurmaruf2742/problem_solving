from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_list=[]
        i = 0
        for j in range(1,len(nums)):
            if nums[i]==nums[j]:
                if nums[j] not in nums:
                    nums[i]=nums[j]
                i += 1
            else:
                nums[i]=nums[i]
                i += 1

        return nums
sol = Solution()
print(sol.removeDuplicates([1,1,2,3]))

