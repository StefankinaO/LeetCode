class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        ans_word1, ans_word2 = '', ''
        for i in range(len(word1)):
            ans_word1 += word1[i]
        for i in range(len(word2)):
            ans_word2 += word2[i]
        return ans_word1 == ans_word2
