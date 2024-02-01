from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0

        for customer_wealth in accounts:
            current_wealth = sum(customer_wealth)
            max_wealth = max(max_wealth, current_wealth)

        return max_wealth
        # another version
        # r_sum=0
        # rich_customers=[]
        # for i in accounts:
        #     for j in range(len(i)):
        #         r_sum += i[j]
        #     rich_customers.append(r_sum)
        #     r_sum=0
        # return (max(rich_customers))
#     time complexity of this code is O(n*m)
#     space complexity of this code is O(n) because i use additional list = rich_customer



a=Solution()
print(a.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))