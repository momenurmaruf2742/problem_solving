from typing import List
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ls=Counter(nums)
        ls2=max(ls,key=ls.get)
       
        return ls2

a=Solution
print(a.majorityElement(None,[3,2,3]))