class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word=s.split()
        return len(word[-1])

a=Solution
a.lengthOfLastWord(None,"   fly me   to   the moon  ")