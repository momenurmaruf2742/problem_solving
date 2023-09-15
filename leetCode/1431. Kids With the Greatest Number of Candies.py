from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        largest_number=None
        for number in candies:
            if largest_number is None or largest_number < number:
                largest_number = number
        return [x + extraCandies >= largest_number for x in candies]


print(Solution.kidsWithCandies(None,[1,12,5,4],1))