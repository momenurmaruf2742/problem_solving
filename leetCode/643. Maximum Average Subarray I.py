from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # print(dir(nums))
        for i in range(k+1):

            print(nums.remove(max(nums)))


        print((nums))
        
a=Solution
print(a.findMaxAverage(None,[1,12,-5,-6,50,3],3))