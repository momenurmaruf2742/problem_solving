from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = [x for x in nums if x > 4 or abs(x) > 4]
        result = sum(result)/k
        print(result)
        
a=Solution
print(a.findMaxAverage(None,[1,12,-5,-6,50,3],4))