from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
<<<<<<< HEAD
        for i in List:


        pass

        return


c = Solution
print(c.productExceptSelf(None,[145,665,66]))
=======
        n = len(nums)
        left = [1] * n
        right = [1] * n
        result = [0] * n

        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        for i in range(n):
            result[i] = left[i] * right[i]

        return result
#     time complexity of this code is O(n)
#     space complexity of this code is O(n)
c = Solution()
print(c.productExceptSelf([-1,1,0,-3,3]))


>>>>>>> 9a3d17bb881f3290dfe42ef7b60ebceff1fd2bae
