from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_list= [element for element in nums if element != val]
        nums[:]=new_list

        return len(new_list)







a = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
a.removeElement(nums,val)
print(a.removeElement(nums,val))