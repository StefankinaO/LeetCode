class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_str = str(n)
        summa, multiply = 0, 1
        for i in range(len(n_str)):
            summa += int(n_str[i])
            multiply *= int(n_str[i])
        return multiply - summa

