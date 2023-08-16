class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_num = ''
    
        for value, symbol in roman_dict.items():
            while num >= value:
                roman_num += symbol
                num -= value
                
        return roman_num

a=Solution
print(a.intToRoman(None,6))