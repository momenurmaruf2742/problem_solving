from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Total sum of the array
        left_sum = 0  # Initial left sum (empty array)
        valid_splits = 0  # Counter for valid splits

        # Iterate over the array, excluding the last element
        for i in range(len(nums) - 1):
            left_sum += nums[i]  # Add the current element to the left sum
            right_sum = total_sum - left_sum  # Calculate the right sum
            if left_sum >= right_sum:  # Check if left sum is greater than or equal to right sum
                valid_splits += 1  # Count this valid split

        return valid_splits
solu = Solution()
print(solu.waysToSplitArray([10,4,-8,7]))