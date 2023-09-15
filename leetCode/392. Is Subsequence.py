class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_i = 0

        for char in t:
            if s_i < len(s) and char == s[s_i]:
                s_i += 1
        return s_i == len(s)


a=Solution
print(a.isSubsequence(None,"acb","ahbgdc"))