class Solution:
    def numberOfSteps (self, num: int) -> int:
        chet = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
                chet += 1
            else:
                num -=1
                chet += 1
        return chet
