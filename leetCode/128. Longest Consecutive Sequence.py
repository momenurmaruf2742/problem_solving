from typing import List

"""Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time."""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):

