class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(ransomNote)):
            count = +magazine.count(ransomNote[i])
            print("magazine",ransomNote[i])
            print(count)
            count2 = +ransomNote.count(ransomNote[i])
            print("ransomnote",ransomNote[i])
            print(count2)
            # if ransomNote[i] in magazine:
            #     if count>count2 or count == count2:
            #         return True
            #     elif count2>count:
            #         return False
            #     else:
            #         return False
            # else:
            #     count = magazine.count(ransomNote[i])
            #     print(count)
            #     return False





c = Solution
print(c.canConstruct(None,"fihjjjjei","hjibagacbhadfaefdjaeaebgi"))


