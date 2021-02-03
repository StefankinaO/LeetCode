class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) >= 3:
            max1 = max(nums)
            nums.remove(max1)
            max2 = max(nums)
            nums.remove(max2)
            max3 = max(nums)
            return max3
        elif len(nums) <= 2:
            return max(nums)