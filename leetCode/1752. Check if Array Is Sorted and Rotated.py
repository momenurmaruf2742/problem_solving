from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        # n = len(nums)

        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                count += 1
            if count > 1:
                return False

        return True


solution = Solution()
print(solution.check([6,7,7,5]))