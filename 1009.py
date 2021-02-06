class Solution:
    def bitwiseComplement(self, N: int) -> int:
        get_bin = lambda x: format(x, 'b')
        binir = get_bin(N)
        ans = ''
        for i in range(len(binir)):
            if binir[i] == "1":
                ans += "0"
            else:
                ans += "1"
        return int(ans, 2)
