class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxim = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if maxim < (nums[i]-1)*(nums[j]-1):
                        maxim = (nums[i]-1)*(nums[j]-1)
        return maxim
