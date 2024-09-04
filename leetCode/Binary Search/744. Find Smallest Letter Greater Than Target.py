from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        start = 0
        end = len(letters) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if letters[mid] > target:
                end = mid - 1
            if letters[mid] <= target:
                start = mid + 1
        return letters[start]

        # if target >= letters[-1] or target < letters[0]:
        #     return letters[0]
        #
        # low = 0
        # high = len(letters) - 1
        # while low <= high:
        #     mid = (high + low) // 2
        #
        #     if target >= letters[mid]:  # in binary search this would be only greater than
        #         low = mid + 1
        #
        #     if target < letters[mid]:
        #         high = mid - 1
        #
        # return letters[low]

sol = Solution()
print(sol.nextGreatestLetter(["c","f","j"],"d"))