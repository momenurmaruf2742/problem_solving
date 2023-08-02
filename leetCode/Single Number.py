from typing import List
from collections import Counter
class Solution:
    def singleNumber(self,nums: List[int]) -> int:
        
        ls=Counter(nums)
        for key in ls:
            if ls[key]==1:
                return key
a=Solution
a.singleNumber(None,[1,1,2,3,3,4,4,4])