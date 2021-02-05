class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxim = [0]
        for i in range(len(gain)):
            maxim.append(maxim[i] + gain[i])
        return max(maxim)