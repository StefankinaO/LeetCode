class Solution:
    def reverse(self, x: int) -> int:
        if x < 0 :
            x = str(x)
            x = x[1:]
            x = (-1) * int(x[::-1])
            if -2 ** (31) > x:
                return 0
            else:
                return x
        else:
            x = str(x)
            x = int(x[::-1])
            if x > 2**(31) - 1:
                return 0
            else:
                return x
