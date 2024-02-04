
class Solution:
    def reverseWords(self, s: str) -> str:
        return (" ".join(s.split()[::-1]))

c = Solution
print(c.reverseWords(None," new g"))