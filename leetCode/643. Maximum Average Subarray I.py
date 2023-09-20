from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = [x for x in nums if x >= k or abs(x) >= k]
        result = sum(result)/k
        print(result)
        
a=Solution
print(a.findMaxAverage(None,[-1],1))