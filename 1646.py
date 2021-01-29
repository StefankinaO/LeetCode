class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = []
        nums.insert(0, 0)
        nums.insert(1, 1)
        for i in range(1, n - 1):
            nums.insert(2*i, nums[i])
            nums.insert(2*i + 1, nums[i]+ nums[i + 1])
        return max(nums[:n + 1])
