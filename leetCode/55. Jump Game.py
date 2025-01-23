from math import trunc
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        elements= 0
        for i in nums:
            if elements < 0:
                return False
            elif elements < i:
                elements = i
            elements -= 1
        return True



solution = Solution()
print(solution.canJump(nums=[3,2,1,0,4]))