from typing import List
from collections import Counter
class Solution:
    def singleNumber(self,nums: List[int]) -> int:
        ls2=[]
        ls=Counter(nums)
        print(ls)
        for key in ls:
            if ls[key]==1:
                ls2.append(key)
    
        return ls2
a=Solution
print(a.singleNumber(None,[1,1,2,3,3,4,4,4,5]))