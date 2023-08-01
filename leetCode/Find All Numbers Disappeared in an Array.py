from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        b= list(nums)
        n= len(b)
        re=[]
        for i in range(1,n+1):
            if i not in b:
                re.append(i)
        return re


a=Solution
print(a.findDisappearedNumbers(None,[4,3,2,7,8,2,3,1]))