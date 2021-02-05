class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i] == stones[j]:
                    ans += 1
        return ans
