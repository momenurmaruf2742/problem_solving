from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Step 1: Helper function to check if a word is a vowel string
        def is_vowel_string(word):
            return word[0] in vowels and word[-1] in vowels

        # Step 2: Compute the prefix sum array
        n = len(words)
        prefix_sum = [0] * n
        prefix_sum[0] = 1 if is_vowel_string(words[0]) else 0

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + (1 if is_vowel_string(words[i]) else 0)

        # Step 3: Answer each query
        result = []
        for l, r in queries:
            if l == 0:
                result.append(prefix_sum[r])
            else:
                result.append(prefix_sum[r] - prefix_sum[l - 1])

        return result

sol=Solution()
print(sol.vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]))