from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices)<2:
            return 0
        mpr=0
        mip=prices[0]
        for p in prices[1:]:
            mpr=max(mpr,p-mip)
            mip=min(mip,p)
        return mpr
        
a=Solution
a.maxProfit(None,[7,1])