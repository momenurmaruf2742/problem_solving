class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev_value = 0
        running_sum = 0
        
        for i in range(len(s)-1, -1, -1):
            curr_value = roman_dict[s[i]]
            if curr_value < prev_value:
                running_sum -= curr_value
            else:
                running_sum += curr_value
            prev_value = curr_value
        
        return running_sum
s=Solution()
print(s.romanToInt("MCMXCIV"))  # Output: 1994