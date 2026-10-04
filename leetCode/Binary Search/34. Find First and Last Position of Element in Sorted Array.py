from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        start, end = 0, len(nums) - 1
        newidx = []
        while start <= end:
            mid = (start + end) // 2
            newidx.append(mid)
            if nums[mid] == target:
                newidx.append(mid)
            elif nums[mid] > target:
                start = mid + 1
            else:
                end = mid - 1
        return newidx


sol = Solution()
print(
    sol.searchRange([5,7,7,8,8,10],8)
)