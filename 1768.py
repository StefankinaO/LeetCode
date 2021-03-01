class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        n = min(len(word1), len(word2))
        for i in range(n):
            ans += word1[i] +word2[i]
        if len(word1) > len(word2):
            ans += word1[len(word2):]
        if len(word1) < len(word2):
            ans += word2[len(word1):]
        return ans