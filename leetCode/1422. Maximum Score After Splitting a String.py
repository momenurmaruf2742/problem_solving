class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count('1')

        left_zeros = 0
        max_count = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                left_zeros += 1
            else:
                total_ones -= 1
            total = left_zeros + total_ones
            max_count = max(max_count, total)
        return max_count



sol = Solution()
print(sol.maxScore("011101"))

"""
Time Complexity**: * `s.count('1')`: O(n) 
* Traversing the string: 
* Total: O(n). 
* **Space Complexity**: 
* O(1): Only a few variables are used (no additional data structures).



"""