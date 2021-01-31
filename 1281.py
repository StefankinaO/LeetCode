class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        summa = sum(accounts[0])
        for i in range(1, len(accounts)):
            if summa < sum(accounts[i]):
                summa = sum(accounts[i])
        return summa
