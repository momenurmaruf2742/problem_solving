from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        for i in range (len(nums)):
            if nums[i] % 2 == nums[i+1] % 2 :
                return False

        return True



s = Solution()
print(s.isArraySpecial([4,3,1,6]))


