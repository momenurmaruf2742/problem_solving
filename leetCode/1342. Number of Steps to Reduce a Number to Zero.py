class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps=0
        while(num >0 ):
            if num % 2 == 0:
                num //=2
            else:
                num -=1
            steps +=1
        return steps
# time complexity of this code is O(logn)
# space complexity of this code is O(1)

c = Solution
print(c.numberOfSteps(None,14))