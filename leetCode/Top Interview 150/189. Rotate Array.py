from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            for j in range(len(nums)-1, 0, -1):
                nums[j], nums[j-1] = nums[j-1], nums[j]

        return nums


sol = Solution()
print(sol.rotate([1,2,3,4,5,6,7], k = 3))
