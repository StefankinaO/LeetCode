class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dictionar = {}
        ans = ''
        k = 0
        for i in indices:
            dictionar[i] = s[k]
            k+= 1
        dictionar = dict(sorted(dictionar.items()))
        for key in dictionar:
            ans += str(dictionar[key])
        return ans
