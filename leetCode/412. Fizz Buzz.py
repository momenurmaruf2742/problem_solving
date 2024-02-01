from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list_fizz_buzz=["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for i in range(1, n + 1)]

        # another aproch
        # for i in range(1,n+1):
        #     if i % 3 == 0 and i % 5 == 0:
        #         list_fizz_buzz.append("FizzBuzz")
        #     elif i % 3 == 0:
        #         list_fizz_buzz.append("Fizz")
        #     elif i % 5 == 0:
        #         list_fizz_buzz.append("Buzz")
        #     else:
        #         list_fizz_buzz.append(str(i))
        return list_fizz_buzz
    # time complexity is O(n)
    # space complexity is O(1) constant
a = Solution
print(a.fizzBuzz(None,3))