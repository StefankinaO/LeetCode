class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        curr_sum = max_sum
        for i, n in enumerate(nums[k:], k):
            curr_sum = curr_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum, curr_sum)
            
        return max_sum/k