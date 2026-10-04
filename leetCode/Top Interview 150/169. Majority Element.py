from typing import List
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        counts = 0
        for i in nums:
            if counts == 0:
                candidate = i
            if i == candidate:
                counts += 1
            else:
                counts -= 1
        return candidate

a=Solution
print(a.majorityElement(None,[3,2,3]))